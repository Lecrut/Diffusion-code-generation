import os
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
from tqdm import tqdm

from ollama import ensure_ollama, ensure_model, save_cache
import instructions
import persistence
import topics
import validator
import codegen as code

NUM_TOPICS = 100
INSTR_PER_TOPIC = 10
MAX_WORKERS = 4
VARIANTS_PER_INSTR = 3
ATTEMPTS_PER_INSTR = 10

DATA_DIR = "data"
DATASET_FILE = "dataset.csv"

os.makedirs(DATA_DIR, exist_ok=True)
CODE_DIR = os.path.join(DATA_DIR, "code")
os.makedirs(CODE_DIR, exist_ok=True)


def save_progress(chunk, partial_results, lock):
    with lock:
        for row in chunk:
            row["id"] = len(partial_results)
            partial_results.append(row)
            if row["code"].strip():
                file_path = os.path.join(CODE_DIR, f"{row['id']}.py")
                persistence.save_code(file_path, row["code"])
        persistence.save_dataset(partial_results, DATASET_FILE)


def build_variants(row):
    variants = code.generate_variants(row["instruction"], attempts=ATTEMPTS_PER_INSTR, desired=VARIANTS_PER_INSTR)
    if not variants:
        fallback = code.generate_one_fallback(row["instruction"], extra_attempts=ATTEMPTS_PER_INSTR)
        if fallback:
            variants = [fallback]
    records = []
    if variants:
        for variant_index, variant in enumerate(variants):
            records.append({
                "topic": row["topic"],
                "instruction": row["instruction"],
                "code": variant,
                "valid": bool(variant),
                "variant_idx": variant_index,
            })
    else:
        records.append({
            "topic": row["topic"],
            "instruction": row["instruction"],
            "code": "",
            "valid": False,
            "variant_idx": 0,
        })
    return records


def validate_codes(df):
    errors = []
    for _, row in df.iterrows():
        file_path = os.path.join(CODE_DIR, f"{row['id']}.py")
        try:
            validator.compile_source(file_path)
            if validator.EXECUTE_DEMOS:
                return_code, stderr = validator.execute_source(file_path, validator.EXEC_TIMEOUT)
                if return_code != 0:
                    errors.append((row["id"], f"runtime_error: {stderr[:2000]}"))
                    df.loc[df.id == row["id"], "valid"] = False
        except Exception as exc:
            errors.append((row["id"], f"compile_error: {exc}"))
            df.loc[df.id == row["id"], "valid"] = False
    return errors


def run(num_topics=NUM_TOPICS, instr_per_topic=INSTR_PER_TOPIC, max_workers=MAX_WORKERS):
    print("Rozpoczynam generowanie datasetu.")
    ensure_ollama()
    ensure_model()

    print(f"Ładuję lub generuję {num_topics} tematów...")
    topics_df = topics.load_or_generate_topics(num_topics=num_topics, force=False)
    print(f"Załadowano {len(topics_df)} tematów.")

    print(f"Ładuję lub generuję {instr_per_topic} instrukcji dla każdego tematu...")
    instr = instructions.load_or_generate_instructions(topics_df, instr_per_topic=instr_per_topic, force=False, max_attempts_per_topic=20)
    print(f"Załadowano {len(instr)} instrukcji.")

    print("Rozpoczynam generowanie kodu...")
    partial_results = []
    save_lock = Lock()

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(build_variants, row) for _, row in instr.iterrows()]
        with tqdm(total=len(futures), desc="Generowanie kodu", unit="instr") as progress:
            for future in as_completed(futures):
                save_progress(future.result(), partial_results, save_lock)
                progress.update(1)

    print("Generowanie kodu zakończone. Waliduję pliki...")
    df = pd.DataFrame(partial_results)
    errors = validate_codes(df)
    df.to_csv(DATASET_FILE, index=False)

    save_cache()

    print("Gotowe!")
    print(df["valid"].value_counts())
    if errors:
        for error in errors[:10]:
            print(error)


if __name__ == "__main__":
    run()
