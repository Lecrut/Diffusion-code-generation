import itertools
import json
import os
import platform
import subprocess
import time
from pathlib import Path
from threading import Lock, local

import requests

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


OLLAMA_URL = "http://localhost:11434"
OLLAMA_API_BASE = os.environ.get("OLLAMA_API_BASE", "").rstrip("/")
OLLAMA_API_KEY = os.environ.get("OLLAMA_API_KEY", "")
USE_OPENAI_COMPAT_API = bool(OLLAMA_API_BASE and OLLAMA_API_KEY)
APPEND_NO_THINK = os.environ.get("OLLAMA_APPEND_NO_THINK", "1").lower() not in {
    "0",
    "false",
    "no",
}
# Set OLLAMA_MODELS to a comma-separated list to spread requests across models.
MODEL = os.environ.get("OLLAMA_MODEL", "qwen2.5-coder:14b")
MODELS = [m.strip() for m in os.environ.get("OLLAMA_MODELS", MODEL).split(",") if m.strip()]
if not MODELS:
    MODELS = [MODEL]

try:
    from path_config import DATA_DIR as DEFAULT_DATA_DIR
except ImportError:
    DEFAULT_DATA_DIR = Path(__file__).resolve().parents[2] / "data"

DATA_DIR = Path(os.environ.get("DATASET_CREATOR_DATA_DIR", DEFAULT_DATA_DIR))
CACHE_FILE = Path(os.environ.get("DATASET_CREATOR_CACHE_FILE", DATA_DIR / "cache.json"))

DATA_DIR.mkdir(parents=True, exist_ok=True)
_thread_state = local()
_cache_lock = Lock()
_model_lock = Lock()
_model_cycle = itertools.cycle(MODELS)


if CACHE_FILE.exists():
    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            CACHE = json.load(f)
    except (OSError, json.JSONDecodeError):
        CACHE = {}
else:
    CACHE = {}


def save_cache():
    with _cache_lock:
        _write_cache_unlocked()


def _write_cache_unlocked():
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(CACHE, f, ensure_ascii=False, indent=2)


def _get_session():
    if not hasattr(_thread_state, "session"):
        _thread_state.session = requests.Session()
    return _thread_state.session


def _next_model():
    with _model_lock:
        return next(_model_cycle)


def is_ollama_running():
    try:
        requests.get(OLLAMA_URL, timeout=2)
        return True
    except:
        return False


def start_ollama():
    system = platform.system()

    if system == "Windows":
        subprocess.Popen(["ollama", "serve"], shell=True)
    else:
        subprocess.Popen(["ollama", "serve"])

    time.sleep(5)


def ensure_ollama():
    if USE_OPENAI_COMPAT_API:
        return

    if not is_ollama_running():
        start_ollama()

    for _ in range(10):
        if is_ollama_running():
            return
        time.sleep(1)

    raise RuntimeError("Ollama did not start")


def ensure_model(model=None):
    if USE_OPENAI_COMPAT_API:
        return

    models_to_check = [model] if model else MODELS
    try:
        r = requests.get(f"{OLLAMA_URL}/api/tags", timeout=5)
        r.raise_for_status()

        data = r.json()
        installed = [m["name"] for m in data.get("models", [])]

        for target in models_to_check:
            if any(m == target or m.startswith(f"{target}:") for m in installed):
                continue

            result = subprocess.run(["ollama", "pull", target], check=False)
            if result.returncode != 0:
                raise RuntimeError(f"ollama pull failed for {target!r}")

    except Exception as exc:
        print(f"OLLAMA MODEL CHECK ERROR: {exc}", flush=True)


REQUEST_TIMEOUT = int(os.environ.get("OLLAMA_REQUEST_TIMEOUT", "120"))


def ollama_generate(
    prompt,
    temperature=0.7,
    model=None,
    use_cache=True,
    seed=None,
    num_predict=2048,
    num_ctx=2048,
    request_timeout=None,
):
    selected_model = model or _next_model()
    cache_key = json.dumps(
        {
            "backend": OLLAMA_API_BASE if USE_OPENAI_COMPAT_API else OLLAMA_URL,
            "model": selected_model,
            "prompt": prompt,
            "temperature": temperature,
            "seed": seed,
            "num_predict": num_predict,
            "num_ctx": num_ctx,
            "append_no_think": APPEND_NO_THINK if USE_OPENAI_COMPAT_API else False,
        },
        sort_keys=True,
    )

    if use_cache:
        with _cache_lock:
            if cache_key in CACHE:
                return CACHE[cache_key]

    try:
        options = {
            "temperature": temperature,
            "num_predict": num_predict,
            "num_ctx": num_ctx,
        }
        if seed is not None:
            options["seed"] = seed

        if USE_OPENAI_COMPAT_API:
            request_prompt = prompt
            if APPEND_NO_THINK and "/no_think" not in request_prompt:
                request_prompt = f"{request_prompt}\n\n/no_think"

            r = _get_session().post(
                f"{OLLAMA_API_BASE}/chat/completions",
                headers={
                    "Authorization": f"Bearer {OLLAMA_API_KEY}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": selected_model,
                    "messages": [{"role": "user", "content": request_prompt}],
                    "temperature": temperature,
                    "stream": False,
                },
                timeout=request_timeout or REQUEST_TIMEOUT,
            )
        else:
            r = _get_session().post(
                f"{OLLAMA_URL}/api/generate",
                json={
                    "model": selected_model,
                    "prompt": prompt,
                    "stream": False,
                    "keep_alive": "1h",
                    "think": False,
                    "options": options,
                },
                timeout=request_timeout or REQUEST_TIMEOUT,
            )
        r.raise_for_status()

        data = r.json()
        if USE_OPENAI_COMPAT_API:
            result = data.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
        else:
            result = data.get("response", "").strip()
        if not result:
            return None

        if use_cache:
            with _cache_lock:
                CACHE[cache_key] = result
                _write_cache_unlocked()
        return result

    except requests.HTTPError as exc:
        body = exc.response.text.strip() if exc.response is not None else ""
        detail = f"{exc}; response={body}" if body else str(exc)
        print(f"OLLAMA ERROR ({selected_model}): {detail}", flush=True)
        return None
    except Exception as exc:
        print(f"OLLAMA ERROR ({selected_model}): {exc}", flush=True)
        return None
