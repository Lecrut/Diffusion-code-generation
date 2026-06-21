import os
import json
import random
import re
import time
from pathlib import Path

import pandas as pd
from tqdm import tqdm
from ollama import ollama_generate

try:
    from path_config import DATA_DIR as DEFAULT_DATA_DIR
except ImportError:
    DEFAULT_DATA_DIR = Path(__file__).resolve().parents[2] / "data"

DATA_DIR = Path(os.environ.get("DATASET_CREATOR_DATA_DIR", DEFAULT_DATA_DIR))
INSTR_FILE = DATA_DIR / "instructions.csv"
INSTRUCTIONS_SAVE_EVERY = int(os.environ.get("INSTRUCTIONS_SAVE_EVERY", "25"))
INSTRUCTIONS_SAVE_EVERY_SECONDS = float(os.environ.get("INSTRUCTIONS_SAVE_EVERY_SECONDS", "60"))
INSTRUCTION_REQUEST_TIMEOUT = int(os.environ.get("INSTRUCTION_REQUEST_TIMEOUT", "60"))
INSTRUCTION_EMPTY_RETRY_LIMIT = int(os.environ.get("INSTRUCTION_EMPTY_RETRY_LIMIT", "2"))

INSTRUCTION_TEMPERATURES = [i * 0.05 for i in range(21)]

INSTRUCTIONS_PROMPT_TEMPLATE = (
    "Topic: '{topic}'.\n"
    "Generate {n} different direct Python coding instructions a user would give to an AI assistant to write the complete, high-quality, and optimized Python code for this topic.\n"
    "RULES:\n"
    "1. Use COMMANDS (e.g., 'Write a robust script...', 'Implement an optimized function...').\n"
    "2. NEVER ask questions.\n"
    "3. Explicitly demand professional, efficient, and best-practice Python code.\n"
    "4. Do NOT ask for comments, docstrings, tutorials, explanations, or well-documented code.\n"
    "5. Do NOT request interactive input, user prompts, stdin reads, or required command-line arguments.\n"
    "6. Prefer deterministic tasks that can be demonstrated with hard-coded sample values.\n"
    "7. Do NOT request CLI tools, argparse, external files, databases, network access, test suites, inheritance-only designs, abstract classes, interfaces, or placeholder methods.\n"
    "8. Output ONLY a valid JSON array of OBJECTS. No markdown or extra text.\n"
    "9. Each object MUST have exactly two keys: 'task_id' (integer) and 'instruction' (string).\n"
    "Example of correct output:\n"
    "[\n"
    "  {{ \"task_id\": 1, \"instruction\": \"Write a highly optimized Python function that calculates the sum of two integers. Ensure the code follows PEP 8 standards.\" }}\n"
    "]\n"
)

os.makedirs(DATA_DIR, exist_ok=True)


def _write_csv_with_retry(df: pd.DataFrame, path: Path, attempts: int = 8) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    last_error = None

    for attempt in range(1, attempts + 1):
        tmp_path = path.with_name(f"{path.name}.{os.getpid()}.{attempt}.tmp")
        try:
            df.to_csv(tmp_path, index=False)
            os.replace(tmp_path, path)
            return
        except OSError as exc:
            last_error = exc
            try:
                if tmp_path.exists():
                    tmp_path.unlink()
            except OSError:
                pass
            time.sleep(min(2.0, 0.2 * attempt))

    raise last_error


def _save_instruction_rows(rows, force=False, state=None) -> None:
    if not rows:
        return

    if state is None:
        state = {"unsaved": 0, "last_save_at": 0.0}

    state["unsaved"] += 1
    now = time.monotonic()
    should_save = (
        force
        or INSTRUCTIONS_SAVE_EVERY <= 1
        or state["unsaved"] >= INSTRUCTIONS_SAVE_EVERY
        or now - state["last_save_at"] >= INSTRUCTIONS_SAVE_EVERY_SECONDS
    )
    if not should_save:
        return

    _write_csv_with_retry(pd.DataFrame(rows), INSTR_FILE)
    state["unsaved"] = 0
    state["last_save_at"] = now

def _normalize_instr(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9\s]", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s


def _topic_slug(topic: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", str(topic).strip().lower()).strip("_")
    if not slug:
        return "task"
    if slug[0].isdigit():
        slug = f"task_{slug}"
    return slug[:40]


def _fallback_instruction_candidates(topic: str) -> list[str]:
    slug = _topic_slug(topic)
    readable_topic = str(topic).strip()
    return [
        f"Implement an optimized Python function named {slug}_transform that performs the core operation for '{readable_topic}' using deterministic hard-coded sample values.",
        f"Write a robust Python function named {slug}_validate that validates input values for '{readable_topic}' and returns normalized data using best-practice error handling.",
        f"Create a compact Python module with a function named {slug}_batch_process that processes a list of sample values related to '{readable_topic}' efficiently.",
        f"Implement a Python class named {slug.title().replace('_', '')}Processor that stores sample data for '{readable_topic}' and exposes methods to update and retrieve computed results.",
        f"Write an efficient Python function named {slug}_summary that calculates summary statistics for hard-coded sample values related to '{readable_topic}'.",
        f"Develop a deterministic Python module that maps sample inputs to outputs for '{readable_topic}' using a dictionary-based lookup where appropriate.",
        f"Implement a pure Python function named {slug}_convert_all that converts or transforms multiple hard-coded sample records for '{readable_topic}' in one pass.",
        f"Create a Python class named {slug.title().replace('_', '')}Manager with methods for adding, updating, and listing hard-coded sample entries related to '{readable_topic}'.",
        f"Write a high-quality Python function named {slug}_compare that compares two hard-coded sample values for '{readable_topic}' and returns a structured result.",
        f"Implement an optimized Python function named {slug}_filter_valid that filters invalid sample records for '{readable_topic}' and returns only valid values.",
        f"Create a standalone Python module that defines reusable constants and a function named {slug}_calculate for '{readable_topic}'.",
        f"Write a robust Python function named {slug}_format_results that converts computed sample results for '{readable_topic}' into clean strings.",
        f"Implement a Python class named {slug.title().replace('_', '')}Calculator with class constants and methods that compute sample outputs for '{readable_topic}'.",
        f"Develop an efficient Python function named {slug}_rank_samples that sorts hard-coded sample values for '{readable_topic}' and returns the ranked result.",
        f"Write a deterministic Python module with a function named {slug}_run_examples that executes multiple hard-coded examples for '{readable_topic}' and returns their outputs.",
        f"Implement a best-practice Python function named {slug}_aggregate that groups hard-coded sample records for '{readable_topic}' and computes aggregate values.",
        f"Create a Python function named {slug}_normalize_many that normalizes a list of hard-coded values related to '{readable_topic}' with strict type validation.",
        f"Write an optimized Python class named {slug.title().replace('_', '')}Store that keeps hard-coded sample records for '{readable_topic}' and supports fast lookup by key.",
        f"Implement a Python function named {slug}_detect_changes that compares two hard-coded sample datasets for '{readable_topic}' and returns the differences.",
        f"Create a concise Python module that solves '{readable_topic}' with one reusable function, hard-coded sample values, and a runnable main block.",
    ]


def _fill_with_fallback_instructions(topic: str, current: list[str], seen: set[str], target_count: int) -> int:
    added = 0
    for cand in _fallback_instruction_candidates(topic):
        if len(current) >= target_count:
            break
        if not _minimal_validator(cand):
            continue
        key = _normalize_instr(cand)
        if key in seen:
            continue
        seen.add(key)
        current.append(cand)
        added += 1
    return added

def _minimal_validator(instr: str) -> bool:
    if not instr or not isinstance(instr, str) or len(instr.split()) < 4:
        return False

    if "?" in instr:
        return False

    if instr.strip().lower().startswith(("how", "what", "why", "can", "please", "would", "should")):
        return False

    lowered = instr.lower()
    rejected_patterns = [
        r"\bwell[- ]documented\b",
        r"\bwell[- ]commented\b",
        r"\bdocstrings?\b",
        r"\bcomments?\b",
        r"\bexplanations?\b",
        r"\btutorial\b",
        r"\bprompts?\s+(?:the\s+)?user\b",
        r"\bcontinuously\s+prompts?\b",
        r"\binteractive\b",
        r"\bcommand[- ]line\b",
        r"\bcli\b",
        r"\bargparse\b",
        r"\bterminal\b",
        r"\binput\(\)",
        r"\bsys\.stdin\b",
        r"\bstdin\b",
        r"\bstandard input\b",
        r"\brequired command[- ]line arguments?\b",
        r"\bfiles?\b",
        r"\bexternal (?:configuration )?files?\b",
        r"\breads?\s+(?:from\s+)?(?:a\s+)?files?\b",
        r"\bwrites?\s+(?:to\s+)?(?:a\s+)?files?\b",
        r"\bfile format\b",
        r"\bdatabase\b",
        r"\bsqlite\b",
        r"\bnetwork\b",
        r"\bapi\b",
        r"\bunit tests?\b",
        r"\btest suite\b",
        r"\bpytest\b",
        r"\bunittest\b",
        r"\bpreviously implemented\b",
        r"\bexisting (?:class|function|module|code)\b",
        r"\binheritance\b",
        r"\binherit(?:s|ing|ance)?\b",
        r"\babstract\b",
        r"\binterface\b",
        r"\bbase class\b",
        r"\boverrid(?:e|es|ing)\b",
        r"\bpolymorphism\b",
        r"\bnot implemented\b",
        r"\bplaceholder\b",
        r"\bstub\b",
    ]
    if any(re.search(pattern, lowered) for pattern in rejected_patterns):
        return False

    return True

def _extract_json_array(text: str) -> list:
    start = text.find('[')
    if start == -1:
        return []

    end = text.rfind(']')
    if end != -1 and end > start:
        json_str = text[start:end+1]
        try:
            return json.loads(json_str)
        except json.JSONDecodeError:
            pass

    partial = text[start:]
    if not partial.endswith(']'):
        partial = partial + ']' 
    try:
        return json.loads(partial)
    except json.JSONDecodeError:
        return []

def load_or_generate_instructions(topics_df, instr_per_topic=10, force=False, max_attempts_per_topic=20):
    existing = {}
    if os.path.exists(INSTR_FILE) and not force:
        try:
            df_existing = pd.read_csv(INSTR_FILE)
            for _, r in df_existing.iterrows():
                tid = int(r["topic_id"]) if "topic_id" in r else None
                existing.setdefault(tid, []).append(str(r["instruction"]))
        except Exception:
            existing = {}

    rows = []
    save_state = {"unsaved": 0, "last_save_at": 0.0}
    
    for _, row in tqdm(topics_df.iterrows(), total=len(topics_df), desc="Generowanie instrukcji"):
        tid = int(row["topic_id"])
        topic = row["topic"]
        current = []
        seen = set()
        
        for x in existing.get(tid, []):
            if _minimal_validator(x):
                key = _normalize_instr(x)
                if key not in seen:
                    seen.add(key)
                    current.append(x)

        attempts = 0
        no_new_attempts = 0
        
        while len(current) < instr_per_topic and attempts < max_attempts_per_topic:
            need = instr_per_topic - len(current)
            request_n = min(10, need)
            temperature = random.choice(INSTRUCTION_TEMPERATURES)
            
            prompt = INSTRUCTIONS_PROMPT_TEMPLATE.format(topic=topic, n=request_n)

            if no_new_attempts >= 3:
                prompt = (
                    f"Topic: '{topic}'.\n"
                    f"Generate {need} direct Python coding instructions for this topic, demanding high-quality and optimized code.\n"
                    "Do not ask questions, comments, docstrings, explanations, interactive prompts, stdin reads, required CLI arguments, files, databases, tests, inheritance, abstract classes, interfaces, or placeholders.\n"
                    "Prefer deterministic tasks that can be demonstrated with hard-coded sample values.\n"
                    "Output ONLY a JSON array of objects with keys 'task_id' and 'instruction'."
                )

            text = ollama_generate(
                prompt,
                temperature,
                request_timeout=INSTRUCTION_REQUEST_TIMEOUT,
            )
            attempts += 1
            
            if not text:
                no_new_attempts += 1
                if no_new_attempts >= INSTRUCTION_EMPTY_RETRY_LIMIT:
                    added = _fill_with_fallback_instructions(topic, current, seen, instr_per_topic)
                    print(
                        f"[INSTRUCTIONS] fallback filled {added} instructions for topic_id={tid} "
                        f"after {no_new_attempts} empty/timeout responses",
                        flush=True,
                    )
                    break
                continue

            candidates = _extract_json_array(text)
            new_count = 0
            
            for item in candidates:
                if not isinstance(item, dict) or "instruction" not in item:
                    continue
                    
                cand = str(item["instruction"]).strip()
                
                if not _minimal_validator(cand):
                    continue
                    
                key = _normalize_instr(cand)
                if key in seen:
                    continue
                    
                seen.add(key)
                current.append(cand)
                new_count += 1
                
                if len(current) >= instr_per_topic:
                    break

            if new_count == 0:
                no_new_attempts += 1
                if no_new_attempts >= INSTRUCTION_EMPTY_RETRY_LIMIT:
                    added = _fill_with_fallback_instructions(topic, current, seen, instr_per_topic)
                    print(
                        f"[INSTRUCTIONS] fallback filled {added} instructions for topic_id={tid} "
                        f"after {no_new_attempts} no-new responses",
                        flush=True,
                    )
                    break
            else:
                no_new_attempts = 0

        if len(current) < instr_per_topic:
            added = _fill_with_fallback_instructions(topic, current, seen, instr_per_topic)
            if added:
                print(
                    f"[INSTRUCTIONS] fallback completed topic_id={tid} with {added} local instructions",
                    flush=True,
                )

        for i, instr in enumerate(current):
            rows.append({
                "topic_id": tid,
                "instruction_id": i,
                "topic": topic,
                "instruction": instr
            })

        _save_instruction_rows(rows, state=save_state)

    _save_instruction_rows(rows, force=True, state=save_state)
    return pd.DataFrame(rows)
