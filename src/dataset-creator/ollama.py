import requests
import os
import time
import json
import subprocess # Możesz zostawić, jeśli używasz go gdzieś indziej, ale tu już nie będzie potrzebny
import platform
from threading import Lock

DATA_PATH = "data2"
OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434")
MODEL = "gemma4:e4b"
CACHE_FILE = "cache.json"

os.makedirs(DATA_PATH, exist_ok=True)
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