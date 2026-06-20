import itertools
import json
import os
import platform
import re
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


PROXY_API_BASE = "https://pkapust.iis.p.lodz.pl/ollama_piat/v1"
PROXY_CHAT_URL = "https://pkapust.iis.p.lodz.pl/ollama_piat/api/chat"
PROXY_MODEL = "qwen3.5:122b-a10b"
PROXY_API_KEYS = [
    "supersilnetymczasowehasloalamakota1",
    "supersilnetymczasowehasloalamakota2",
    "supersilnetymczasowehasloalamakota3",
]
OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434")
OLLAMA_BACKEND = os.environ.get("OLLAMA_BACKEND", "proxy").strip().lower()
OLLAMA_API_BASE = os.environ.get(
    "OLLAMA_API_BASE",
    PROXY_API_BASE if OLLAMA_BACKEND in {"proxy", "remote"} else OLLAMA_URL,
)
OLLAMA_PROXY_CHAT_URL = os.environ.get(
    "OLLAMA_PROXY_CHAT_URL",
    PROXY_CHAT_URL if OLLAMA_BACKEND in {"proxy", "remote"} else "",
).strip()
# Set OLLAMA_MODELS to a comma-separated list to spread requests across models.
MODEL = os.environ.get("OLLAMA_MODEL", PROXY_MODEL if OLLAMA_BACKEND == "proxy" else "qwen2.5-coder:14b")


def _looks_like_path(value: str) -> bool:
    normalized = value.strip()
    if not normalized:
        return False
    if os.path.isabs(normalized):
        return True
    return "\\" in normalized or normalized.startswith("./") or normalized.startswith("../")


def _resolve_models():
    raw_models = os.environ.get("OLLAMA_MODELS", "")
    if raw_models and _looks_like_path(raw_models):
        print(
            f"[OLLAMA CONFIG] ignoring OLLAMA_MODELS path value={raw_models}; using OLLAMA_MODEL={MODEL}",
            flush=True,
        )
        return [MODEL]

    if raw_models:
        parsed_models = [m.strip() for m in raw_models.split(",") if m.strip()]
        if parsed_models:
            return parsed_models

    return [MODEL]


def _resolve_api_keys() -> list[str]:
    raw_keys = os.environ.get("OLLAMA_API_KEYS", "").strip()
    if raw_keys:
        parsed = [k.strip() for k in raw_keys.split(",") if k.strip()]
        if parsed:
            return parsed

    fallback_key = os.environ.get("OLLAMA_API_KEY", "").strip()
    if fallback_key:
        return [fallback_key]

    if OLLAMA_BACKEND in {"proxy", "remote"}:
        return list(PROXY_API_KEYS)

    if OLLAMA_API_BASE.rstrip("/") == PROXY_API_BASE.rstrip("/"):
        return list(PROXY_API_KEYS)

    return []


MODELS = _resolve_models()
API_KEYS = _resolve_api_keys()

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
_key_lock = Lock()
_key_cycle = itertools.cycle(API_KEYS or [""])
_config_log_lock = Lock()
_config_logged = False


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


def _next_api_key():
    with _key_lock:
        return next(_key_cycle)


def _is_proxy_backend():
    if OLLAMA_BACKEND in {"proxy", "remote"}:
        return True
    if OLLAMA_BACKEND == "local":
        return False
    return OLLAMA_API_BASE.rstrip("/") == PROXY_API_BASE.rstrip("/")


def _effective_api_base():
    if _is_proxy_backend():
        return OLLAMA_API_BASE.rstrip("/")
    return OLLAMA_URL.rstrip("/")


def _effective_proxy_chat_url():
    if OLLAMA_PROXY_CHAT_URL:
        return OLLAMA_PROXY_CHAT_URL.rstrip("/")

    base = _effective_api_base()
    if base.endswith("/v1"):
        return f"{base[:-3]}/api/chat"
    return f"{base}/api/chat"


def _effective_api_key(selected_key: str = ""):
    if not _is_proxy_backend():
        return ""
    if selected_key:
        return selected_key
    return _next_api_key()


def _proxy_headers(selected_key: str = ""):
    api_key = _effective_api_key(selected_key)
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    return headers


def _backend_source_label():
    return "proxy" if _is_proxy_backend() else "local"


def _log_backend_config_once():
    global _config_logged
    with _config_log_lock:
        if _config_logged:
            return
        print(
            f"[OLLAMA CONFIG] source={_backend_source_label()} base={_effective_api_base()} chat={_effective_proxy_chat_url() if _is_proxy_backend() else '-'} models={MODELS} api_keys={len(API_KEYS)}",
            flush=True,
        )
        _config_logged = True


def is_ollama_running():
    if _is_proxy_backend():
        return True
    try:
        requests.get(OLLAMA_URL, timeout=2)
        return True
    except:
        return False


def start_ollama():
    if _is_proxy_backend():
        return
    system = platform.system()

    if system == "Windows":
        subprocess.Popen(["ollama", "serve"], shell=True)
    else:
        subprocess.Popen(["ollama", "serve"])

    time.sleep(5)


def ensure_ollama():
    _log_backend_config_once()
    if _is_proxy_backend():
        print(f"[OLLAMA READY] source=proxy base={_effective_api_base()}", flush=True)
        return
    if not is_ollama_running():
        start_ollama()

    for _ in range(10):
        if is_ollama_running():
            print(f"[OLLAMA READY] source=local base={_effective_api_base()}", flush=True)
            return
        time.sleep(1)

    raise RuntimeError("Ollama did not start")


def ensure_model(model=None):
    _log_backend_config_once()
    if _is_proxy_backend():
        target = model or MODEL
        print(f"[OLLAMA MODEL] source=proxy model={target}", flush=True)
        return
    models_to_check = [model] if model else MODELS
    try:
        r = requests.get(f"{OLLAMA_URL}/api/tags", timeout=5)
        r.raise_for_status()

        data = r.json()
        installed = [m["name"] for m in data.get("models", [])]

        for target in models_to_check:
            if any(m == target or m.startswith(f"{target}:") for m in installed):
                print(f"[OLLAMA MODEL] source=local model={target} status=installed", flush=True)
                continue

            result = subprocess.run(["ollama", "pull", target], check=False)
            if result.returncode != 0:
                raise RuntimeError(f"ollama pull failed for {target!r}")
            print(f"[OLLAMA MODEL] source=local model={target} status=pulled", flush=True)

    except Exception as exc:
        print(f"OLLAMA MODEL CHECK ERROR: {exc}", flush=True)


REQUEST_TIMEOUT = int(os.environ.get("OLLAMA_REQUEST_TIMEOUT", "120"))


def _extract_proxy_text(payload: dict) -> str:
    if not isinstance(payload, dict):
        return ""

    # Native Ollama /api/chat shape.
    direct = payload.get("message", {})
    if isinstance(direct, dict):
        text = str(direct.get("content", "") or "").strip()
        if text:
            return text

    # OpenAI-style fallback shape.
    choices = payload.get("choices")
    if isinstance(choices, list) and choices:
        first = choices[0] or {}
        if isinstance(first, dict):
            message = first.get("message", {})
            if isinstance(message, dict):
                return str(message.get("content", "") or "").strip()
    return ""


def _response_has_useful_content(result: str) -> bool:
    text = (result or "").strip()
    if len(text) < 3:
        return False

    lowered = text.lower()
    if lowered.startswith("<html"):
        return False
    if re.match(r"^\s*(error|http\s*\d{3}|status\s*\d{3})\b", lowered):
        return False
    return True


def ollama_generate(
    prompt,
    temperature=0.7,
    model=None,
    use_cache=True,
    seed=None,
    num_predict=2048,
    num_ctx=2048,
):
    selected_model = model or _next_model()
    selected_key = _next_api_key() if _is_proxy_backend() else ""
    key_slot = ""
    if selected_key:
        key_slot = f"k{API_KEYS.index(selected_key) + 1}" if selected_key in API_KEYS else "k?"
    _log_backend_config_once()
    cache_key = json.dumps(
        {
            "model": selected_model,
            "backend": _backend_source_label(),
            "key_slot": key_slot,
            "prompt": prompt,
            "temperature": temperature,
            "seed": seed,
            "num_predict": num_predict,
            "num_ctx": num_ctx,
        },
        sort_keys=True,
    )

    if use_cache:
        with _cache_lock:
            if cache_key in CACHE:
                print(
                    f"[OLLAMA REQUEST] source={_backend_source_label()} model={selected_model} cache=hit",
                    flush=True,
                )
                return CACHE[cache_key]

    print(
        f"[OLLAMA REQUEST] source={_backend_source_label()} model={selected_model} key={key_slot or '-'} cache=miss",
        flush=True,
    )

    try:
        if _is_proxy_backend():
            r = _get_session().post(
                _effective_proxy_chat_url(),
                headers=_proxy_headers(selected_key),
                json={
                    "messages": [
                        {
                            "role": "user",
                            "content": f"{prompt}\n\n/no_think",
                        }
                    ],
                    "stream": False,
                },
                timeout=REQUEST_TIMEOUT,
            )
        else:
            options = {
                "temperature": temperature,
                "num_predict": num_predict,
                "num_ctx": num_ctx,
            }
            if seed is not None:
                options["seed"] = seed

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
                timeout=REQUEST_TIMEOUT,
            )
        r.raise_for_status()

        payload = r.json()
        if _is_proxy_backend():
            result = _extract_proxy_text(payload)
        else:
            result = payload.get("response", "").strip()
        if not _response_has_useful_content(result):
            print(
                f"OLLAMA ERROR ({selected_model}): response missing useful content; payload_keys={list(payload)[:6]}",
                flush=True,
            )
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
