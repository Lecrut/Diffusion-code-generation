import requests
import pandas as pd
from tqdm import tqdm
import os
import time
import json
import subprocess
import platform
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading


OLLAMA_URL = "http://localhost:11434"
MODEL = "gemma4:e2b"

NUM_TOPICS = 50
INSTR_PER_TOPIC = 5
MAX_WORKERS = 1
MAX_RETRIES = 3

DATA_DIR = "data"
CACHE_FILE = "cache.json"
DATASET_FILE = "dataset.csv"

TOPICS_FILE = f"{DATA_DIR}/topics.csv"
INSTR_FILE = f"{DATA_DIR}/instructions.csv"

os.makedirs(DATA_DIR, exist_ok=True)

lock = threading.Lock()

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

    print("Uruchamiam Ollamę...")
    time.sleep(5)


def ensure_ollama():
    if not is_ollama_running():
        start_ollama()

    for _ in range(10):
        if is_ollama_running():
            print("Ollama działa")
            return
        time.sleep(1)

    raise RuntimeError("Ollama nie wystartowała")


def ensure_model():
    try:
        r = requests.get(f"{OLLAMA_URL}/api/tags", timeout=5)
        r.raise_for_status()

        data = r.json()
        models = [m["name"] for m in data.get("models", [])]

        if any(m.startswith(MODEL) for m in models):
            print(f"Model {MODEL} już jest")
            return

        print(f"Pobieram model {MODEL}...")
        subprocess.run(["ollama", "pull", MODEL])

    except Exception as e:
        print(f"Błąd sprawdzania modeli: {e}")


if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        CACHE = json.load(f)
else:
    CACHE = {}

def save_cache():
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(CACHE, f, ensure_ascii=False, indent=2)


def ollama_generate(prompt, temperature=0.7):
    if prompt in CACHE:
        return CACHE[prompt]

    try:
        r = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False, 
                "options": {
                    "temperature": temperature,
                    "num_predict": 500  
                }
            },
            timeout=6000
        )
        r.raise_for_status()

        result = r.json().get("response", "").strip()
        if not result:
            return None

        CACHE[prompt] = result
        return result

    except Exception as e:
        print(f"Błąd {e} generowania dla promptu: {prompt}...")
        return None


def is_valid(code):
    try:
        exec(code, {})
        return True
    except:
        return False


def load_or_generate_topics():
    if os.path.exists(TOPICS_FILE):
        print("Wczytuję tematy")
        return pd.read_csv(TOPICS_FILE)

    print("Generuję tematy...")
    prompt = f"Wygeneruj {NUM_TOPICS} tematów zadań Python. Jedna linia = jeden temat."

    text = ollama_generate(prompt, 0.8)

    if text is None:
        raise RuntimeError("Brak tematów")

    topics = [t.strip("- ").strip() for t in text.split("\n") if t.strip()]

    df = pd.DataFrame({
        "topic_id": range(len(topics)),
        "topic": topics[:NUM_TOPICS]
    })

    df.to_csv(TOPICS_FILE, index=False)
    return df


def load_or_generate_instructions(topics_df):
    if os.path.exists(INSTR_FILE):
        print("Wczytuję instrukcje")
        return pd.read_csv(INSTR_FILE)

    print("Generuję instrukcje...")
    rows = []

    for _, row in tqdm(topics_df.iterrows(), total=len(topics_df)):
        prompt = f"Dla tematu: {row['topic']} wygeneruj {INSTR_PER_TOPIC} instrukcji."

        text = ollama_generate(prompt, 0.9)
        if text is None:
            continue

        instructions = [i.strip("- ").strip() for i in text.split("\n") if i.strip()]

        for i, instr in enumerate(instructions[:INSTR_PER_TOPIC]):
            rows.append({
                "topic_id": row["topic_id"],
                "instruction_id": i,
                "topic": row["topic"],
                "instruction": instr
            })

    df = pd.DataFrame(rows)
    df.to_csv(INSTR_FILE, index=False)
    return df


def generate_code(instruction):
    prompt = f"Napisz działający kod Python:\n{instruction}\nTylko kod."
    return ollama_generate(prompt, 0.2)


def generate_valid_code(instruction):
    for _ in range(MAX_RETRIES):
        code = generate_code(instruction)
        if code and is_valid(code):
            return code

    return code or ""


def process_row(idx, row):
    code = generate_valid_code(row["instruction"])

    return {
        "id": idx,
        "topic": row["topic"],
        "instruction": row["instruction"],
        "code": code,
        "valid": is_valid(code)
    }


def run():
    ensure_ollama()
    ensure_model()

    topics = load_or_generate_topics()
    instr = load_or_generate_instructions(topics)

    print("Generuję kod...")

    results = []

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [
            executor.submit(process_row, idx, row)
            for idx, row in instr.iterrows()
        ]

        for f in tqdm(as_completed(futures), total=len(futures)):
            results.append(f.result())

    df = pd.DataFrame(results)
    df.to_csv(DATASET_FILE, index=False)

    save_cache()

    print("Gotowe!")
    print(df["valid"].value_counts())


if __name__ == "__main__":
    run()