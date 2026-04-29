import os
import json
import random
import re
import pandas as pd
from tqdm import tqdm
from ollama import ollama_generate

DATA_DIR = "data"
INSTR_FILE = f"{DATA_DIR}/instructions.csv"

INSTRUCTION_TEMPERATURES = [i * 0.05 for i in range(21)]

INSTRUCTIONS_PROMPT_TEMPLATE = (
    "Topic: '{topic}'.\n"
    "Generate {n} different direct Python coding instructions a user would give to an AI assistant to write the complete, high-quality, and optimized Python code for this topic.\n"
    "RULES:\n"
    "1. Use COMMANDS (e.g., 'Write a robust script...', 'Implement an optimized function...').\n"
    "2. NEVER ask questions.\n"
    "3. Explicitly demand professional, efficient, and best-practice Python code.\n"
    "4. Output ONLY a valid JSON array of OBJECTS. No markdown or extra text.\n"
    "5. Each object MUST have exactly two keys: 'task_id' (integer) and 'instruction' (string).\n"
    "Example of correct output:\n"
    "[\n"
    "  {{ \"task_id\": 1, \"instruction\": \"Write a highly optimized Python function that calculates the sum of two integers. Ensure the code follows PEP 8 standards.\" }}\n"
    "]\n"
)

os.makedirs(DATA_DIR, exist_ok=True)

def _normalize_instr(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9\s]", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s

def _minimal_validator(instr: str) -> bool:
    if not instr or not isinstance(instr, str) or len(instr.split()) < 4:
        return False

    if "?" in instr:
        return False

    if instr.strip().lower().startswith(("how", "what", "why", "can", "please", "would", "should")):
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
                    "Do not ask questions.\n"
                    "Output ONLY a JSON array of objects with keys 'task_id' and 'instruction'."
                )

            text = ollama_generate(prompt, temperature)
            attempts += 1
            
            if not text:
                no_new_attempts += 1
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
            else:
                no_new_attempts = 0

        for i, instr in enumerate(current):
            rows.append({
                "topic_id": tid,
                "instruction_id": i,
                "topic": topic,
                "instruction": instr
            })

        pd.DataFrame(rows).to_csv(INSTR_FILE, index=False)

    return pd.DataFrame(rows)