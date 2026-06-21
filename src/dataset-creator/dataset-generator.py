import argparse
import importlib.util
import os
import re
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from threading import Lock

import pandas as pd
from tqdm import tqdm

import codegen as code
import instructions
import persistence
import topics
from ollama import backend_summary, ensure_model, ensure_ollama, save_cache

try:
    from path_config import DATA_DIR as DEFAULT_DATA_DIR
except ImportError:
    DEFAULT_DATA_DIR = Path(__file__).resolve().parents[2] / "data"


NUM_TOPICS = int(os.environ.get("DATASET_NUM_TOPICS", "50"))
INSTR_PER_TOPIC = int(os.environ.get("DATASET_INSTR_PER_TOPIC", "5"))
VARIANTS_PER_INSTR = int(os.environ.get("DATASET_VARIANTS_PER_INSTR", "3"))
ATTEMPTS_PER_INSTR = int(os.environ.get("DATASET_ATTEMPTS_PER_INSTR", "60"))
MAX_WORKERS = int(os.environ.get("DATASET_GENERATOR_WORKERS", "3"))
AUTO_COMMIT_ENABLED = os.environ.get("DATASET_GENERATOR_AUTO_COMMIT", "0").lower() in {
    "1",
    "true",
    "yes",
}
SAVE_DATASET_EVERY = int(os.environ.get("DATASET_SAVE_EVERY", "20"))
SAVE_DATASET_EVERY_SECONDS = float(os.environ.get("DATASET_SAVE_EVERY_SECONDS", "60"))
ALLOW_CODE_OVERWRITE = os.environ.get("DATASET_ALLOW_CODE_OVERWRITE", "0").lower() in {
    "1",
    "true",
    "yes",
}
KEEP_OBSOLETE_ROWS = os.environ.get("DATASET_KEEP_OBSOLETE_ROWS", "0").lower() in {
    "1",
    "true",
    "yes",
}

DATA_DIR = Path(os.environ.get("DATASET_CREATOR_DATA_DIR", DEFAULT_DATA_DIR))
DATASET_FILE = DATA_DIR / "dataset.csv"
CODE_DIR = DATA_DIR / "code"

DATA_DIR.mkdir(parents=True, exist_ok=True)
CODE_DIR.mkdir(parents=True, exist_ok=True)
_last_dataset_save_at = 0.0
_unsaved_dataset_rows = 0


def _clean_cell(value) -> str:
    if value is None:
        return ""
    try:
        if pd.isna(value):
            return ""
    except TypeError:
        pass
    return str(value)


def _safe_int(value, default=0) -> int:
    if value is None:
        return default
    try:
        if pd.isna(value):
            return default
    except TypeError:
        pass
    try:
        return int(float(value))
    except (TypeError, ValueError):
        return default


def _truthy(value) -> bool:
    if isinstance(value, bool):
        return value
    if value is None:
        return False
    try:
        if pd.isna(value):
            return False
    except TypeError:
        pass
    return str(value).strip().lower() in {"1", "true", "yes"}


def _normalize_instruction_text(value) -> str:
    return " ".join(_clean_cell(value).strip().lower().split())


def _code_file_name(topic_id: int, instruction_id: int, variant_idx: int) -> str:
    base_name = f"{topic_id}_{instruction_id}"
    if variant_idx > 0:
        return f"{base_name}_{variant_idx}.py"
    return f"{base_name}.py"


def _parse_code_file_name(file_name: str):
    match = re.fullmatch(r"(\d+)_(\d+)(?:_(\d+))?\.py", file_name)
    if not match:
        return None
    topic_id = int(match.group(1))
    instruction_id = int(match.group(2))
    variant_idx = int(match.group(3) or 0)
    return topic_id, instruction_id, variant_idx


def _load_auto_commit():
    auto_commit_path = Path(__file__).resolve().parents[1] / "tools" / "autoCommit.py"
    spec = importlib.util.spec_from_file_location("autoCommit", auto_commit_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _read_code_file(file_name: str) -> str:
    if not file_name:
        return ""
    file_path = CODE_DIR / file_name
    if not file_path.exists():
        return ""
    try:
        return file_path.read_text(encoding="utf-8")
    except OSError:
        return ""


def _allocate_code_file(topic_id: int, instruction_id: int, variant_idx: int, code_text: str):
    if ALLOW_CODE_OVERWRITE:
        return variant_idx, _code_file_name(topic_id, instruction_id, variant_idx)

    requested_variant_idx = variant_idx
    while True:
        file_name = _code_file_name(topic_id, instruction_id, variant_idx)
        file_path = CODE_DIR / file_name
        if not file_path.exists():
            if variant_idx != requested_variant_idx:
                print(
                    f"[SAVE] avoiding overwrite: using {file_name} instead of "
                    f"{_code_file_name(topic_id, instruction_id, requested_variant_idx)}",
                    flush=True,
                )
            return variant_idx, file_name

        try:
            if file_path.read_text(encoding="utf-8") == code_text:
                return variant_idx, file_name
        except OSError:
            pass

        variant_idx += 1


def save_dataset_snapshot(partial_results):
    global _last_dataset_save_at, _unsaved_dataset_rows

    persistence.save_dataset(partial_results, DATASET_FILE)
    _last_dataset_save_at = time.monotonic()
    _unsaved_dataset_rows = 0


def save_progress(chunk, partial_results, lock, force=False):
    global _unsaved_dataset_rows

    with lock:
        for row in chunk:
            row = dict(row)
            code_text = _clean_cell(row.get("code"))
            topic_id = _safe_int(row.get("topic_id"))
            instruction_id = _safe_int(row.get("instruction_id"))
            variant_idx = _safe_int(row.get("variant_idx"))
            is_valid = _truthy(row.get("valid"))
            if code_text and is_valid:
                variant_idx, file_name = _allocate_code_file(
                    topic_id,
                    instruction_id,
                    variant_idx,
                    code_text,
                )
            else:
                file_name = _code_file_name(topic_id, instruction_id, variant_idx) if code_text else ""

            row["topic_id"] = topic_id
            row["instruction_id"] = instruction_id
            row["variant_idx"] = variant_idx
            row["id"] = len(partial_results)
            row["code_file"] = file_name
            partial_results.append(row)

            if code_text and is_valid:
                persistence.save_code(CODE_DIR / file_name, code_text)
                print(f"Saved code file: {file_name}", flush=True)
            else:
                print(f"No valid code for: {topic_id}_{instruction_id}", flush=True)

        _unsaved_dataset_rows += len(chunk)
        now = time.monotonic()
        should_save = (
            force
            or SAVE_DATASET_EVERY <= 1
            or _unsaved_dataset_rows >= SAVE_DATASET_EVERY
            or now - _last_dataset_save_at >= SAVE_DATASET_EVERY_SECONDS
        )
        if should_save:
            save_dataset_snapshot(partial_results)


def load_existing_dataset():
    if not DATASET_FILE.exists():
        return []

    try:
        existing = pd.read_csv(DATASET_FILE)
    except Exception:
        return []

    records = existing.to_dict("records")
    invalid_count = 0
    recovered_from_file = 0

    for row in records:
        code_text = _clean_cell(row.get("code"))
        file_code = _read_code_file(_clean_cell(row.get("code_file")))
        if file_code:
            if file_code != code_text:
                recovered_from_file += 1
            code_text = file_code
            row["code"] = code_text

        validation = code.validate_code(
            code_text,
            execute=False,
            instruction=_clean_cell(row.get("instruction")),
        )
        row["compile_valid"] = validation.compile_ok
        row["valid"] = validation.ok
        row["validation_error"] = "" if validation.ok else validation.error

        if code_text and not validation.ok:
            invalid_count += 1

    if recovered_from_file:
        print(f"Loaded code text for {recovered_from_file} rows from saved files.", flush=True)
    if invalid_count:
        print(f"Found {invalid_count} existing rows that do not pass validation; they will be regenerated.", flush=True)

    return records


def filter_current_instruction_records(records, instr_df):
    if not records:
        return records

    current_instructions = {}
    for _, row in instr_df.iterrows():
        key = (_safe_int(row.get("topic_id"), -1), _safe_int(row.get("instruction_id"), -1))
        current_instructions[key] = _normalize_instruction_text(row.get("instruction"))

    kept = []
    dropped = 0
    for row in records:
        key = (_safe_int(row.get("topic_id"), -1), _safe_int(row.get("instruction_id"), -1))
        current_instruction = current_instructions.get(key)
        if not current_instruction:
            dropped += 1
            continue
        if _normalize_instruction_text(row.get("instruction")) != current_instruction:
            dropped += 1
            continue
        kept.append(row)

    if dropped:
        print(
            f"Dropped {dropped} existing rows for obsolete or regenerated instructions.",
            flush=True,
        )

    return kept


def build_existing_state(records):
    existing_keys = defaultdict(set)
    existing_examples = defaultdict(list)
    next_variant_idx = defaultdict(int)

    for path in CODE_DIR.glob("*.py"):
        parsed = _parse_code_file_name(path.name)
        if parsed is None:
            continue
        topic_id, instruction_id, variant_idx = parsed
        next_variant_idx[(topic_id, instruction_id)] = max(
            next_variant_idx[(topic_id, instruction_id)],
            variant_idx + 1,
        )

    for row in records:
        topic_id = _safe_int(row.get("topic_id"), default=-1)
        instruction_id = _safe_int(row.get("instruction_id"), default=-1)
        if topic_id < 0 or instruction_id < 0:
            continue

        key = (topic_id, instruction_id)
        variant_idx = _safe_int(row.get("variant_idx"))
        next_variant_idx[key] = max(next_variant_idx[key], variant_idx + 1)

        if not _truthy(row.get("valid")):
            continue

        variant_key = code.normalize_variant(_clean_cell(row.get("code")))
        if variant_key:
            existing_keys[key].add(variant_key)
            if len(existing_examples[key]) < 6:
                existing_examples[key].append(_clean_cell(row.get("code")))

    return existing_keys, existing_examples, next_variant_idx


def _variant_record(row, topic_id, instruction_id, variant_idx, variant):
    return {
        "topic_id": topic_id,
        "instruction_id": instruction_id,
        "topic": row["topic"],
        "instruction": row["instruction"],
        "code": variant,
        "valid": True,
        "compile_valid": True,
        "runtime_valid": code.VALIDATE_BY_EXECUTION,
        "validation_error": "",
        "variant_idx": variant_idx,
    }


def build_variants(row, save_variant=None):
    topic_id = _safe_int(row["topic_id"])
    instruction_id = _safe_int(row["instruction_id"])
    task_label = f"{topic_id}_{instruction_id}"
    needed = _safe_int(row.get("_variants_needed"), VARIANTS_PER_INSTR)
    variant_start = _safe_int(row.get("_variant_start"))
    attempts_per_instr = _safe_int(row.get("_attempts_per_instr"), ATTEMPTS_PER_INSTR)
    existing_keys = row.get("_existing_variant_keys") or set()
    existing_examples = row.get("_existing_variant_examples") or []
    records = []

    def on_variant(variant, offset):
        record = _variant_record(row, topic_id, instruction_id, variant_start + offset, variant)
        if save_variant is not None:
            save_variant(record)
        else:
            records.append(record)

    print(f"Starting generation for {task_label}; need {needed} variants", flush=True)
    variants = code.generate_variants(
        row["instruction"],
        min_unique=needed,
        max_attempts=attempts_per_instr,
        existing_keys=existing_keys,
        existing_examples=existing_examples,
        on_variant=on_variant,
    )

    if variants and save_variant is not None:
        records = []

    if not variants:
        records.append(
            {
                "topic_id": topic_id,
                "instruction_id": instruction_id,
                "topic": row["topic"],
                "instruction": row["instruction"],
                "code": "",
                "valid": False,
                "compile_valid": False,
                "runtime_valid": False,
                "validation_error": f"no valid variants after {attempts_per_instr} attempts",
                "variant_idx": variant_start,
            }
        )

    print(f"Finished generation for {task_label}, variants={len(variants)}", flush=True)
    return records


def run(
    num_topics=NUM_TOPICS,
    instr_per_topic=INSTR_PER_TOPIC,
    variants_per_instr=VARIANTS_PER_INSTR,
    attempts_per_instr=ATTEMPTS_PER_INSTR,
    max_workers=MAX_WORKERS,
):
    print("Rozpoczynam generowanie datasetu.")
    print(f"Data directory: {DATA_DIR}")
    print(f"LLM backend: {backend_summary()}")
    print(
        f"Run target: topics={num_topics}, instructions/topic={instr_per_topic}, "
        f"variants/instruction={variants_per_instr}, attempts/instruction={attempts_per_instr}, "
        f"workers={max_workers}"
    )
    ensure_ollama()
    ensure_model()

    auto_commit = None
    if AUTO_COMMIT_ENABLED:
        auto_commit = _load_auto_commit()
        auto_commit.start_scheduler(20)

    partial_results = []
    try:
        print(f"Laduje lub generuje {num_topics} tematow...")
        topics_df = topics.load_or_generate_topics(num_topics=num_topics, force=False)
        print(f"Zaladowano {len(topics_df)} tematow.")

        print(f"Laduje lub generuje {instr_per_topic} instrukcji dla kazdego tematu...")
        instr = instructions.load_or_generate_instructions(
            topics_df,
            instr_per_topic=instr_per_topic,
            force=False,
            max_attempts_per_topic=20,
        )
        print(f"Zaladowano {len(instr)} instrukcji.")

        partial_results = load_existing_dataset()
        if KEEP_OBSOLETE_ROWS:
            print("Keeping obsolete dataset rows because DATASET_KEEP_OBSOLETE_ROWS is enabled.", flush=True)
        else:
            partial_results = filter_current_instruction_records(partial_results, instr)
        existing_keys, existing_examples, next_variant_idx = build_existing_state(partial_results)
        completed_count = sum(1 for keys in existing_keys.values() if len(keys) >= variants_per_instr)
        if partial_results:
            print(
                f"Wznawiam generacje: {completed_count} instrukcji ma juz "
                f"{variants_per_instr} poprawnych wariantow.",
                flush=True,
            )

        pending = []
        for _, row in instr.iterrows():
            topic_id = int(row["topic_id"])
            instruction_id = int(row["instruction_id"])
            key = (topic_id, instruction_id)
            valid_count = len(existing_keys.get(key, set()))
            needed = max(0, variants_per_instr - valid_count)
            if needed == 0:
                continue

            item = row.to_dict()
            item["_variants_needed"] = needed
            item["_variant_start"] = next_variant_idx.get(key, 0)
            item["_attempts_per_instr"] = attempts_per_instr
            item["_existing_variant_keys"] = set(existing_keys.get(key, set()))
            item["_existing_variant_examples"] = list(existing_examples.get(key, []))
            pending.append(item)

        print(
            f"Rozpoczynam generowanie kodu dla {len(pending)} instrukcji "
            f"(workers={max_workers}, variants_per_instr={variants_per_instr})."
        )
        save_lock = Lock()

        if pending:
            worker_count = max(1, min(max_workers, len(pending)))
            def save_variant(record):
                save_progress([record], partial_results, save_lock)

            with ThreadPoolExecutor(max_workers=worker_count) as executor:
                futures = {
                    executor.submit(build_variants, row, save_variant): (row["topic_id"], row["instruction_id"])
                    for row in pending
                }
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

        print("Generowanie kodu zakonczone. Zapisuje wynik...")
        save_dataset_snapshot(partial_results)
        df = pd.DataFrame(partial_results)

        print("Gotowe!")
        if "valid" in df:
            print(df["valid"].value_counts())
        return df
    finally:
        if partial_results:
            save_dataset_snapshot(partial_results)
        save_cache()
        if auto_commit is not None:
            auto_commit.stop_scheduler()


def parse_args():
    parser = argparse.ArgumentParser(description="Generate compile-validated Python code dataset variants.")
    parser.add_argument("--num-topics", type=int, default=NUM_TOPICS)
    parser.add_argument("--instr-per-topic", type=int, default=INSTR_PER_TOPIC)
    parser.add_argument("--variants-per-instr", type=int, default=VARIANTS_PER_INSTR)
    parser.add_argument("--attempts-per-instr", type=int, default=ATTEMPTS_PER_INSTR)
    parser.add_argument("--workers", type=int, default=MAX_WORKERS)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    run(
        num_topics=args.num_topics,
        instr_per_topic=args.instr_per_topic,
        variants_per_instr=args.variants_per_instr,
        attempts_per_instr=args.attempts_per_instr,
        max_workers=args.workers,
    )
