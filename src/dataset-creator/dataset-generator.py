import os
import pandas as pd
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

from ollama import ensure_ollama, ensure_model, save_cache
import topics
import instructions
import code


NUM_TOPICS = 100
INSTR_PER_TOPIC = 10
MAX_WORKERS = 4
CODE_MAX_RETRIES = 3
VARIANTS_PER_INSTR = 3
ATTEMPTS_PER_INSTR = 10

DATA_DIR = "data"
DATASET_FILE = "dataset.csv"

os.makedirs(DATA_DIR, exist_ok=True)

# Save each code variant to files and optionally execute demo to validate
CODE_DIR = f"{DATA_DIR}/code"
os.makedirs(CODE_DIR, exist_ok=True)

# runtime check settings
EXECUTE_DEMOS = True
EXEC_TIMEOUT = 5  # seconds per file


def run(num_topics=NUM_TOPICS, instr_per_topic=INSTR_PER_TOPIC, max_workers=MAX_WORKERS,
    code_retries=CODE_MAX_RETRIES):
    ensure_ollama()
    ensure_model()

    # force regenerate topics and instructions to ensure exact counts
    topics_df = topics.load_or_generate_topics(num_topics=num_topics, force=True, max_attempts=50)
    instr = instructions.load_or_generate_instructions(topics_df, instr_per_topic=instr_per_topic, force=True, max_attempts_per_topic=20)

    print("Generuję kod...")

    results = []

    def worker(idx, row):
        out = []
        variants = code.generate_variants(row["instruction"], attempts=ATTEMPTS_PER_INSTR, desired=VARIANTS_PER_INSTR)
        if not variants:
            # fallback: try to get at least one valid code
            fb = code.generate_one_fallback(row["instruction"], extra_attempts=ATTEMPTS_PER_INSTR)
            if fb:
                variants = [fb]
        for vi, v in enumerate(variants):
            out.append({
                "topic": row["topic"],
                "instruction": row["instruction"],
                "code": v,
                "valid": True if v else False,
                "variant_idx": vi,
            })
        # ensure at least one record (even if invalid) so counts match
        if not out:
            out.append({
                "topic": row["topic"],
                "instruction": row["instruction"],
                "code": "",
                "valid": False,
                "variant_idx": 0,
            })
        return out

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(worker, idx, row) for idx, row in instr.iterrows()]

        for f in tqdm(as_completed(futures), total=len(futures)):
            results.extend(f.result())

    # assign sequential ids
    for i, r in enumerate(results):
        r["id"] = i

    df = pd.DataFrame(results)
    df.to_csv(DATASET_FILE, index=False)

    # assign sequential ids
    for i, r in enumerate(results):
        r["id"] = i

    df = pd.DataFrame(results)

    # save code files and optionally execute demos for validation
    run_errors = []
    for _, row in df.iterrows():
        file_name = f"{row['id']}.py"
        file_path = os.path.join(CODE_DIR, file_name)
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(row["code"])
        except Exception as e:
            run_errors.append((row["id"], str(e)))
            continue

        # compile check
        try:
            import py_compile
            py_compile.compile(file_path, doraise=True)
        except Exception as e:
            run_errors.append((row["id"], f"compile_error: {e}"))
            df.loc[df.id == row["id"], "valid"] = False
            continue

        if EXECUTE_DEMOS:
            # run file in subprocess with timeout
            import subprocess
            try:
                proc = subprocess.run(["python", file_path], capture_output=True, timeout=EXEC_TIMEOUT)
                if proc.returncode != 0:
                    err = proc.stderr.decode("utf-8", errors="ignore")[:2000]
                    run_errors.append((row["id"], f"runtime_error: {err}"))
                    df.loc[df.id == row["id"], "valid"] = False
            except subprocess.TimeoutExpired:
                run_errors.append((row["id"], "timeout"))
                df.loc[df.id == row["id"], "valid"] = False
            except Exception as e:
                run_errors.append((row["id"], f"exec_error: {e}"))
                df.loc[df.id == row["id"], "valid"] = False

    df.to_csv(DATASET_FILE, index=False)

    save_cache()

    print("Gotowe!")
    print(df["valid"].value_counts())

    if run_errors:
        print("Some files failed compile/run checks. Examples:")
        for i, err in run_errors[:10]:
            print(i, err)


if __name__ == "__main__":
    run()