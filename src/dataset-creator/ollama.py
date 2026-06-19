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


PROXY_API_BASE = "https://pkapust.iis.p.lodz.pl/ollama_piat/v1"

# qwen3.6:27b
PROXY_MODEL = "qwen3.6:27b"
PROXY_API_KEY = "supersilnetymczasowehasloalamakota1"

# qwen3.6:35b
# PROXY_MODEL = "qwen3.6:35b"
# PROXY_API_KEY = "supersilnetymczasowehasloalamakota2"

# qwen3.5:122b-a10b
# PROXY_MODEL = "qwen3.5:122b-a10b"
# PROXY_API_KEY = "supersilnetymczasowehasloalamakota3"
OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434")
OLLAMA_BACKEND = os.environ.get("OLLAMA_BACKEND", "proxy").strip().lower()
OLLAMA_API_BASE = os.environ.get(
    "OLLAMA_API_BASE",
    PROXY_API_BASE if OLLAMA_BACKEND in {"proxy", "remote"} else OLLAMA_URL,
)
OLLAMA_API_KEY = os.environ.get(
    "OLLAMA_API_KEY",
    PROXY_API_KEY if OLLAMA_BACKEND in {"proxy", "remote"} else "",
)
NO_THINK_DIRECTIVE = os.environ.get("OLLAMA_NO_THINK_DIRECTIVE", "/no_think")
NO_THINK_ALIASES = {"/no_think", "/nothink"}
import re as _re
_THINK_BLOCK_RE = _re.compile(r"<think>[\s\S]*?</think>", _re.IGNORECASE)

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


MODELS = _resolve_models()

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


def _effective_api_key():
    if not _is_proxy_backend():
        return ""
    return OLLAMA_API_KEY or PROXY_API_KEY


def _proxy_headers():
    api_key = _effective_api_key()
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    return headers


def _backend_source_label():
    return "proxy" if _is_proxy_backend() else "local"


def _with_no_think(prompt: str) -> str:
    text = (prompt or "").rstrip()
    if not text:
        return NO_THINK_DIRECTIVE
    lines = [line.strip().lower() for line in text.splitlines() if line.strip()]
    if any(line in NO_THINK_ALIASES for line in lines):
        return text
    return f"{text}\n\n{NO_THINK_DIRECTIVE}"


def _log_backend_config_once():
    global _config_logged
    with _config_log_lock:
        if _config_logged:
            return
        print(
            f"[OLLAMA CONFIG] source={_backend_source_label()} base={_effective_api_base()} models={MODELS}",
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


REQUEST_TIMEOUT = int(os.environ.get("OLLAMA_REQUEST_TIMEOUT", "240"))
CONNECT_TIMEOUT = float(os.environ.get("OLLAMA_CONNECT_TIMEOUT", "20"))
READ_TIMEOUT = float(os.environ.get("OLLAMA_READ_TIMEOUT", str(REQUEST_TIMEOUT)))
REQUEST_RETRIES = int(os.environ.get("OLLAMA_REQUEST_RETRIES", "2"))
RETRY_BACKOFF_SECONDS = float(os.environ.get("OLLAMA_RETRY_BACKOFF_SECONDS", "3"))
RETRY_BACKOFF_MAX_SECONDS = float(os.environ.get("OLLAMA_RETRY_BACKOFF_MAX_SECONDS", "20"))
RETRYABLE_HTTP_STATUS = {408, 429, 500, 502, 503, 504}


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
    _log_backend_config_once()
    cache_key = json.dumps(
        {
            "model": selected_model,
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
        f"[OLLAMA REQUEST] source={_backend_source_label()} model={selected_model} cache=miss",
        flush=True,
    )

    max_attempts = max(1, REQUEST_RETRIES + 1)
    last_detail = "unknown error"

    for attempt in range(1, max_attempts + 1):
        try:
            if attempt > 1:
                print(
                    f"[OLLAMA RETRY] model={selected_model} attempt={attempt}/{max_attempts}",
                    flush=True,
                )

            if _is_proxy_backend():
                r = _get_session().post(
                    f"{_effective_api_base()}/chat/completions",
                    headers=_proxy_headers(),
                    json={
                        "model": selected_model,
                        "temperature": temperature,
                        "messages": [
                            {
                                "role": "user",
                                "content": _with_no_think(prompt),
                            }
                        ],
                    },
                    timeout=(CONNECT_TIMEOUT, READ_TIMEOUT),
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
                    timeout=(CONNECT_TIMEOUT, READ_TIMEOUT),
                )

            if r.status_code in RETRYABLE_HTTP_STATUS and attempt < max_attempts:
                last_detail = f"HTTP {r.status_code}: {r.text[:300]}"
                wait_seconds = min(RETRY_BACKOFF_SECONDS * (2 ** (attempt - 1)), RETRY_BACKOFF_MAX_SECONDS)
                print(
                    f"[OLLAMA RETRYABLE] model={selected_model} status={r.status_code} wait={wait_seconds:.1f}s",
                    flush=True,
                )
                time.sleep(wait_seconds)
                continue

            r.raise_for_status()

            payload = r.json()
            if _is_proxy_backend():
                message = payload.get("choices", [{}])[0].get("message", {})
                result = message.get("content", "").strip()
                reasoning = message.get("reasoning_content", "")
                if reasoning:
                    print(
                        f"[OLLAMA THINKING] model={selected_model} reasoning_chars={len(reasoning)}",
                        flush=True,
                    )
                result = _THINK_BLOCK_RE.sub("", result).strip()
            else:
                result = payload.get("response", "").strip()

            if not result:
                last_detail = "empty response payload"
                break

            if use_cache:
                with _cache_lock:
                    CACHE[cache_key] = result
                    _write_cache_unlocked()
            return result

        except requests.HTTPError as exc:
            body = exc.response.text.strip() if exc.response is not None else ""
            last_detail = f"{exc}; response={body}" if body else str(exc)
            status_code = exc.response.status_code if exc.response is not None else None
            if status_code in RETRYABLE_HTTP_STATUS and attempt < max_attempts:
                wait_seconds = min(RETRY_BACKOFF_SECONDS * (2 ** (attempt - 1)), RETRY_BACKOFF_MAX_SECONDS)
                print(
                    f"[OLLAMA RETRYABLE] model={selected_model} status={status_code} wait={wait_seconds:.1f}s",
                    flush=True,
                )
                time.sleep(wait_seconds)
                continue
            break
        except (requests.Timeout, requests.ConnectionError) as exc:
            last_detail = str(exc)
            if attempt < max_attempts:
                wait_seconds = min(RETRY_BACKOFF_SECONDS * (2 ** (attempt - 1)), RETRY_BACKOFF_MAX_SECONDS)
                print(
                    f"[OLLAMA RETRYABLE] model={selected_model} error={exc.__class__.__name__} wait={wait_seconds:.1f}s",
                    flush=True,
                )
                time.sleep(wait_seconds)
                continue
            break
        except Exception as exc:
            last_detail = str(exc)
            break

    print(f"OLLAMA ERROR ({selected_model}): {last_detail}", flush=True)
    return None
