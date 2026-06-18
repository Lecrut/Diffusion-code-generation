import requests
import os
import time
import json
from threading import Lock

def _sanitize_for_filename(value: str) -> str:
    return "".join(ch if ch.isalnum() or ch in ("-", "_") else "_" for ch in value)


OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://10.24.16.27:11434")
MODEL = os.environ.get("OLLAMA_MODEL", "qwen3.6:27b")
DATA_PATH = os.environ.get("DATASET_CREATOR_DATA_DIR", "data2")
CACHE_FILE = os.environ.get(
    "DATASET_CREATOR_CACHE_FILE",
    os.path.join(DATA_PATH, f"cache_{_sanitize_for_filename(MODEL)}.json"),
)
REQUEST_TIMEOUT = int(os.environ.get("OLLAMA_REQUEST_TIMEOUT", "300"))

os.makedirs(DATA_PATH, exist_ok=True)
cache_dir = os.path.dirname(CACHE_FILE)
if cache_dir:
    os.makedirs(cache_dir, exist_ok=True)
session = requests.Session()
ollama_lock = Lock()

if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        CACHE = json.load(f)
else:
    CACHE = {}

def save_cache():
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(CACHE, f, ensure_ascii=False, indent=2)

def is_ollama_running():
    try:
        requests.get(OLLAMA_URL, timeout=2)
        return True
    except:
        return False

def start_ollama():
    # Zmiana 2: Docker sam dba o start kontenera Ollama, my tylko grzecznie czekamy
    print("Oczekuję na uruchomienie kontenera Ollama...", flush=True)
    time.sleep(5)

def ensure_model():
    # Zmiana 3: Pobieranie modelu przez HTTP API zamiast subprocess
    try:
        r = requests.get(f"{OLLAMA_URL}/api/tags", timeout=5)
        r.raise_for_status()

        data = r.json()
        models = [m["name"] for m in data.get("models", [])]

        if any(m.startswith(MODEL) for m in models):
            return

        print(f"Model {MODEL} nie został znaleziony. Zlecam pobieranie przez API (to może potrwać)...", flush=True)
        pull_req = requests.post(f"{OLLAMA_URL}/api/pull", json={"name": MODEL}, stream=True)
        for line in pull_req.iter_lines():
            if line:
                status = json.loads(line).get("status", "")
                print(f"[Ollama Pull] {status}", flush=True)

    except Exception as e:
        print(f"Błąd podczas weryfikacji/pobierania modelu: {e}", flush=True)
        return

def ensure_ollama():
    print("Sprawdzam połączenie z Ollamą...", flush=True)
    if not is_ollama_running():
        start_ollama()

    # Czekamy aż kontener z Ollamą będzie gotowy
    for _ in range(15):
        if is_ollama_running():
            print("Połączono z Ollamą w Dockerze!", flush=True)
            return
        time.sleep(2)

    raise RuntimeError("Nie udało się połączyć z Ollamą. Upewnij się, że kontener 'ollama' działa poprawnie.")


def get_runtime_config() -> dict:
    return {
        "ollama_url": OLLAMA_URL,
        "model": MODEL,
        "data_path": DATA_PATH,
        "cache_file": CACHE_FILE,
        "request_timeout": REQUEST_TIMEOUT,
    }

def ollama_generate(prompt, temperature=0.7, use_cache=False):
    cache_key = f"{OLLAMA_URL}|||{MODEL}|||{temperature}|||{prompt}"
    
    with ollama_lock:
        if use_cache and cache_key in CACHE:
            return CACHE[cache_key]

        try:
            r = session.post(
                f"{OLLAMA_URL}/api/generate",
                json={
                    "model": MODEL,
                    "prompt": prompt,
                    "stream": False,
                    "keep_alive": "1h",
                    "think": False, 
                    "options": {
                            "temperature": temperature,
                            "num_predict": 2048,
                            "num_ctx": 2048,
                    },
                },
                timeout=REQUEST_TIMEOUT,
            )
            r.raise_for_status()

            result = r.json().get("response", "").strip()
            if not result:
                return None

            # Zapisujemy do cache TYLKO jeśli use_cache to True
            if use_cache:
                CACHE[cache_key] = result
                save_cache() 
                
            return result

        except Exception as exc:
            print(f"OLLAMA ERROR: {exc}", flush=True)
            return None