import requests
import os
import time
import json
import subprocess
import platform
from threading import Lock


OLLAMA_URL = "http://localhost:11434"
MODEL = "gemma4:e2b"

DATA_DIR = "data"
CACHE_FILE = "cache.json"

os.makedirs(DATA_DIR, exist_ok=True)
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
    system = platform.system()

    if system == "Windows":
        subprocess.Popen(["ollama", "serve"], shell=True)
    else:
        subprocess.Popen(["ollama", "serve"])

    time.sleep(5)


def ensure_ollama():
    if not is_ollama_running():
        start_ollama()

    for _ in range(10):
        if is_ollama_running():
            return
        time.sleep(1)

    raise RuntimeError("Ollama did not start")


def ensure_model():
    try:
        r = requests.get(f"{OLLAMA_URL}/api/tags", timeout=5)
        r.raise_for_status()

        data = r.json()
        models = [m["name"] for m in data.get("models", [])]

        if any(m.startswith(MODEL) for m in models):
            return

        subprocess.run(["ollama", "pull", MODEL])

    except Exception:
        return


REQUEST_TIMEOUT = 60


def ollama_generate(prompt, temperature=0.7):
    cache_key = f"{prompt}|||{temperature}"
    
    with ollama_lock:
        if cache_key in CACHE:
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
                        "num_predict": 256,
                        "num_ctx": 2048,
                    },
                },
                timeout=REQUEST_TIMEOUT,
            )
            r.raise_for_status()

            result = r.json().get("response", "").strip()
            if not result:
                return None

            CACHE[cache_key] = result
            save_cache() 
            return result

        except Exception as exc:
            print(f"OLLAMA ERROR: {exc}", flush=True)
            return None
