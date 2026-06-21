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
_API_FORMAT_ALIASES = {
    "native": "ollama",
    "ollama-native": "ollama",
    "ollama_native": "ollama",
    "openai-compatible": "openai",
    "openai_compatible": "openai",
}
_REQUESTED_API_FORMAT = os.environ.get("OLLAMA_API_FORMAT", "auto").strip().lower()
OLLAMA_API_FORMAT = _API_FORMAT_ALIASES.get(_REQUESTED_API_FORMAT, _REQUESTED_API_FORMAT)
if OLLAMA_API_FORMAT not in {"auto", "openai", "ollama"}:
    raise ValueError("OLLAMA_API_FORMAT must be one of: auto, openai, ollama")
USE_REMOTE_API = bool(OLLAMA_API_BASE)


def _env_flag(name, default):
    value = os.environ.get(name)
    if value is None:
        return default
    return value.strip().lower() not in {"0", "false", "no", "off"}


APPEND_NO_THINK = _env_flag("OLLAMA_APPEND_NO_THINK", True)
STREAM_OLLAMA = _env_flag("OLLAMA_STREAM", True)
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
_remote_format_lock = Lock()
_model_cycle = itertools.cycle(MODELS)
_resolved_remote_api_format = None
_printed_openai_fallback_notice = False


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


def _ollama_native_api_base():
    if OLLAMA_API_BASE.lower().endswith("/v1"):
        return OLLAMA_API_BASE[:-3].rstrip("/")
    return OLLAMA_API_BASE


def _ollama_native_endpoint_kind():
    lower_base = OLLAMA_API_BASE.lower().rstrip("/")
    if lower_base.endswith("/api/chat"):
        return "chat"
    return "generate"


def _ollama_native_api_url():
    lower_base = OLLAMA_API_BASE.lower().rstrip("/")
    if lower_base.endswith("/api/generate") or lower_base.endswith("/api/chat"):
        return OLLAMA_API_BASE
    if lower_base.endswith("/api"):
        return f"{OLLAMA_API_BASE}/generate"
    return f"{_ollama_native_api_base()}/api/generate"


def _remote_headers():
    headers = {"Content-Type": "application/json"}
    if OLLAMA_API_KEY:
        headers["Authorization"] = f"Bearer {OLLAMA_API_KEY}"
    return headers


def _request_prompt(prompt):
    if USE_REMOTE_API and APPEND_NO_THINK and "/no_think" not in prompt:
        return f"{prompt}\n\n/no_think"
    return prompt


def _remote_formats_to_try():
    if OLLAMA_API_FORMAT != "auto":
        return [OLLAMA_API_FORMAT]

    lower_base = OLLAMA_API_BASE.lower().rstrip("/")
    if lower_base.endswith("/api") or lower_base.endswith("/api/generate") or lower_base.endswith("/api/chat"):
        return ["ollama"]

    with _remote_format_lock:
        if _resolved_remote_api_format:
            return [_resolved_remote_api_format]

    return ["openai", "ollama"]


def _remember_remote_format(api_format):
    if OLLAMA_API_FORMAT != "auto":
        return

    global _resolved_remote_api_format
    with _remote_format_lock:
        _resolved_remote_api_format = api_format


def _is_unsupported_endpoint(exc):
    response = exc.response
    if response is None or response.status_code != 404:
        return False

    body = response.text.lower()
    return "unsupported endpoint" in body or "not_found" in body or "not found" in body


def _print_openai_fallback_notice():
    global _printed_openai_fallback_notice
    with _remote_format_lock:
        if _printed_openai_fallback_notice:
            return
        _printed_openai_fallback_notice = True

    print(
        "[OLLAMA] OpenAI-compatible endpoint is unsupported; retrying with "
        f"Ollama native endpoint {_ollama_native_api_url()}",
        flush=True,
    )


def _remote_backend_url(api_format):
    if api_format == "openai":
        return f"{OLLAMA_API_BASE}/chat/completions"
    return _ollama_native_api_url()


def _post_remote(api_format, prompt, selected_model, temperature, options, timeout):
    request_prompt = _request_prompt(prompt)
    stream_response = api_format == "ollama" and STREAM_OLLAMA

    if api_format == "openai":
        payload = {
            "model": selected_model,
            "messages": [{"role": "user", "content": request_prompt}],
            "temperature": temperature,
            "stream": False,
        }
    elif _ollama_native_endpoint_kind() == "chat":
        payload = {
            "model": selected_model,
            "messages": [{"role": "user", "content": request_prompt}],
            "stream": stream_response,
            "keep_alive": "1h",
            "think": False,
            "options": options,
        }
    else:
        payload = {
            "model": selected_model,
            "prompt": request_prompt,
            "stream": stream_response,
            "keep_alive": "1h",
            "think": False,
            "options": options,
        }

    return _get_session().post(
        _remote_backend_url(api_format),
        headers=_remote_headers(),
        json=payload,
        stream=stream_response,
        timeout=timeout,
    )


def _extract_ollama_stream_result(response):
    chunks = []
    for line in response.iter_lines(decode_unicode=True):
        if not line:
            continue
        if isinstance(line, bytes):
            line = line.decode("utf-8")

        data = json.loads(line)
        if data.get("error"):
            raise RuntimeError(f"Ollama stream error: {data['error']}")
        if data.get("response"):
            chunks.append(data["response"])
        message = data.get("message")
        if isinstance(message, dict) and message.get("content"):
            chunks.append(message["content"])
        if data.get("done"):
            break

    return "".join(chunks).strip()


def _extract_ollama_result(response, streamed):
    if streamed:
        return _extract_ollama_stream_result(response)
    data = response.json()
    message = data.get("message")
    if isinstance(message, dict):
        return message.get("content", "").strip()
    return data.get("response", "").strip()


def _extract_remote_result(api_format, response):
    if api_format == "openai":
        data = response.json()
        return data.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
    return _extract_ollama_result(response, STREAM_OLLAMA)


def backend_summary():
    if USE_REMOTE_API:
        backend_type = f"remote-{OLLAMA_API_FORMAT}"
        backend = OLLAMA_API_BASE
    else:
        backend_type = "local-ollama"
        backend = OLLAMA_URL
    return f"{backend_type} backend={backend} models={', '.join(MODELS)}"


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
    if USE_REMOTE_API:
        return

    if not is_ollama_running():
        start_ollama()

    for _ in range(10):
        if is_ollama_running():
            return
        time.sleep(1)

    raise RuntimeError("Ollama did not start")


def ensure_model(model=None):
    if USE_REMOTE_API:
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


REQUEST_TIMEOUT = int(os.environ.get("OLLAMA_REQUEST_TIMEOUT", "300"))


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
            "backend": OLLAMA_API_BASE if USE_REMOTE_API else OLLAMA_URL,
            "api_format": OLLAMA_API_FORMAT if USE_REMOTE_API else "local",
            "model": selected_model,
            "prompt": prompt,
            "temperature": temperature,
            "seed": seed,
            "num_predict": num_predict,
            "num_ctx": num_ctx,
            "append_no_think": APPEND_NO_THINK if USE_REMOTE_API else False,
            "stream_ollama": STREAM_OLLAMA,
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

        if USE_REMOTE_API:
            last_http_error = None
            for api_format in _remote_formats_to_try():
                try:
                    r = _post_remote(
                        api_format,
                        prompt,
                        selected_model,
                        temperature,
                        options,
                        request_timeout or REQUEST_TIMEOUT,
                    )
                    r.raise_for_status()
                    _remember_remote_format(api_format)
                    result = _extract_remote_result(api_format, r)
                    break
                except requests.HTTPError as exc:
                    last_http_error = exc
                    if (
                        OLLAMA_API_FORMAT == "auto"
                        and api_format == "openai"
                        and _is_unsupported_endpoint(exc)
                    ):
                        _print_openai_fallback_notice()
                        continue
                    raise
            else:
                raise last_http_error
        else:
            stream_response = STREAM_OLLAMA
            r = _get_session().post(
                f"{OLLAMA_URL}/api/generate",
                json={
                    "model": selected_model,
                    "prompt": prompt,
                    "stream": stream_response,
                    "keep_alive": "1h",
                    "think": False,
                    "options": options,
                },
                stream=stream_response,
                timeout=request_timeout or REQUEST_TIMEOUT,
            )
            r.raise_for_status()
            result = _extract_ollama_result(r, stream_response)
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
