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
VARIANTS_PER_INSTR = 10
ATTEMPTS_PER_INSTR = 100
MAX_WORKERS = 5
DATA_DIR = "data"
DATASET_FILE = os.path.join(DATA_DIR, "dataset.csv")

os.makedirs(DATA_DIR, exist_ok=True)
CODE_DIR = os.path.join(DATA_DIR, "code")
os.makedirs(CODE_DIR, exist_ok=True)


def save_progress(chunk, partial_results, lock):
    with lock:
        for row in chunk:
            row["id"] = len(partial_results)
            base_name = f"{row['topic_id']}_{row['instruction_id']}"
            if row.get("variant_idx", 0) > 0:
                file_name = f"{base_name}_{row['variant_idx']}.py"
            else:
                file_name = f"{base_name}.py"

            row["code_file"] = file_name
            partial_results.append(row)
            if row["code"].strip():
                file_path = os.path.join(CODE_DIR, file_name)
                persistence.save_code(file_path, row["code"])
                print(f"Saved code file: {file_name}", flush=True)
            else:
                print(f"No code for: {file_name}", flush=True)
        persistence.save_dataset(partial_results, DATASET_FILE)


def load_existing_dataset():
    if not os.path.exists(DATASET_FILE):
        return pd.DataFrame()
    try:
        existing = pd.read_csv(DATASET_FILE)
        if "topic_id" in existing.columns and "instruction_id" in existing.columns:
            existing["topic_id"] = existing["topic_id"].astype(int)
            existing["instruction_id"] = existing["instruction_id"].astype(int)
        return existing
    except Exception:
        return pd.DataFrame()


def build_variants(row):
    task_label = f"{row['topic_id']}_{row['instruction_id']}"
    print(f"Starting generation for {task_label}", flush=True)
    variants = code.generate_variants(row["instruction"], min_unique=VARIANTS_PER_INSTR, max_attempts=ATTEMPTS_PER_INSTR)
    if not variants:
        fallback = code.generate_one_fallback(row["instruction"], extra_attempts=ATTEMPTS_PER_INSTR)
        if fallback:
            variants = [fallback]
    records = []
    if variants:
        for variant_index, variant in enumerate(variants):
            records.append({
                "topic_id": row["topic_id"],
                "instruction_id": row["instruction_id"],
                "topic": row["topic"],
                "instruction": row["instruction"],
                "code": variant,
                "valid": bool(variant),
                "variant_idx": variant_index,
            })
    else:
        records.append({
            "topic_id": row["topic_id"],
            "instruction_id": row["instruction_id"],
            "topic": row["topic"],
            "instruction": row["instruction"],
            "code": "",
            "valid": False,
            "variant_idx": 0,
        })

    print(f"Finished generation for {task_label}, variants={len(records)}", flush=True)
    return records


def validate_codes(df):
    errors = []
    for _, row in df.iterrows():
        file_path = os.path.join(CODE_DIR, row["code_file"])
        try:
            validator.compile_source(file_path)
            if validator.EXECUTE_DEMOS:
                return_code, stderr = validator.execute_source(file_path, validator.EXEC_TIMEOUT)
                if return_code != 0:
                    errors.append((row["code_file"], f"runtime_error: {stderr[:2000]}"))
                    df.loc[df.code_file == row["code_file"], "valid"] = False
        except Exception as exc:
            errors.append((row["code_file"], f"compile_error: {exc}"))
            df.loc[df.code_file == row["code_file"], "valid"] = False
    return errors


def run(num_topics=NUM_TOPICS, instr_per_topic=INSTR_PER_TOPIC):
    print("Rozpoczynam generowanie datasetu.")
    os.makedirs(os.path.dirname(DATASET_FILE), exist_ok=True)
    ensure_ollama()
    ensure_model()

    print(f"Ładuję lub generuję {num_topics} tematów...")
    topics_df = topics.load_or_generate_topics(num_topics=num_topics, force=False)
    print(f"Załadowano {len(topics_df)} tematów.")

    print(f"Ładuję lub generuję {instr_per_topic} instrukcji dla każdego tematu...")
    instr = instructions.load_or_generate_instructions(topics_df, instr_per_topic=instr_per_topic, force=False, max_attempts_per_topic=20)
    print(f"Załadowano {len(instr)} instrukcji.")

    existing_df = load_existing_dataset()
    completed_pairs = set()
    if not existing_df.empty:
        for _, old_row in existing_df.iterrows():
            if str(old_row.get("code", "")).strip():
                completed_pairs.add((int(old_row["topic_id"]), int(old_row["instruction_id"])))
        partial_results = existing_df.to_dict("records")
        print(f"Wznawiam generację: {len(completed_pairs)} instrukcji już ma zapisany kod.", flush=True)
    else:
        partial_results = []

    pending = []
    for _, row in instr.iterrows():
        key = (int(row["topic_id"]), int(row["instruction_id"]))
        if key in completed_pairs:
            continue
        pending.append(row)

    print(f"Rozpoczynam generowanie kodu dla {len(pending)} instrukcji...")
    save_lock = Lock()

    if pending:
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = {executor.submit(build_variants, row.to_dict()): (row["topic_id"], row["instruction_id"]) for row in pending}
            with tqdm(total=len(futures), desc="Generowanie kodu", unit="instr") as progress:
                for future in as_completed(futures):
                    task_key = futures[future]
                    try:
                        chunk = future.result()
                    except Exception as exc:
                        print(f"Error generating {task_key[0]}_{task_key[1]}: {exc}", flush=True)
                        chunk = []
                    if chunk:
                        save_progress(chunk, partial_results, save_lock)
                    progress.update(1)
    else:
        print("Brak instrukcji do wygenerowania.", flush=True)

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
