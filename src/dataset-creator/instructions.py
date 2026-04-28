import os
import json
import random
import pandas as pd
from tqdm import tqdm

from ollama import ollama_generate

DATA_DIR = "data"
INSTR_FILE = f"{DATA_DIR}/instructions.csv"

INSTRUCTION_TEMPERATURES = [i * 0.05 for i in range(21)]


INSTRUCTIONS_PROMPT_TEMPLATE = (
    "Topic: '{topic}'.\n"
    "Generate {n} different direct Python coding instructions a user would give to an AI assistant to write the complete Python code for this topic.\n"
    "RULES:\n"
    "1. Use COMMANDS, not questions (e.g., use 'Write a script...', 'Create a function...', 'Build a program...', 'Implement a solution...').\n"
    "2. NEVER ask 'how to', 'what is', 'why', or any other question. Do not explain, describe, or philosophize.\n"
    "3. Keep it beginner-friendly. NO complex math or advanced geometry.\n"
    "4. Each instruction must be exactly 1 to 3 sentences long.\n"
    "5. Start with a verb and mention expected inputs/outputs or the primary task.\n"
    "6. Do not include commentary, examples, specific variable names, or low-level implementation steps.\n"
    "7. Do not break the task into code statements, variable assignments, or intermediate computation steps.\n"
    "CRITICAL FORMATTING: Output ONLY a valid JSON array of strings. No markdown, no extra text.\n"
    "Example of correct output:\n"
    "[\n"
    "  \"Write a Python function that takes two integer inputs and calculates their sum. Print the result.\",\n"
    "  \"Create a script to find the perimeter of a shape. It should take the side lengths as a list and return the total.\"\n"
    "]\n"
    "Example of incorrect output:\n"
    "[\n"
    "  \"Define variable length_a to store the first side length.\",\n"
    "  \"Calculate perimeter_triangle by adding length_a, length_b, and length_c.\"\n"
    "]"
)

os.makedirs(DATA_DIR, exist_ok=True)


def _normalize_instr(s: str) -> str:
    import re
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9\s]", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s


def _minimal_validator(instr: str) -> bool:
    """Minimalna kontrola jakości - odrzuca tylko to, co ewidentnie popsuje kod."""
    words = str(instr).split()
    if len(words) < 8:
        return False
        
    lower_instr = str(instr).lower()
    forbidden_phrases = [
        "explain",
        "describe",
        "user input",
        "interactive",
        "input()",
        "tutorial",
        "define variable",
        "set variable",
        "initialize variable",
        "assign ",
        "store the",
        "by adding",
        "length_a",
        "length_b",
        "length_c",
        "side_length",
        "perimeter_triangle",
        "variable",
        "function name",
    ]
    if any(phrase in lower_instr for phrase in forbidden_phrases):
        return False

    if "?" in instr:
        return False

    if instr.strip().lower().startswith(("how", "what", "why", "can you", "please", "would you", "should")):
        return False

    if instr.strip().endswith("?"):
        return False

    if not instr.strip()[0].isalpha():
        return False

    if "_" in instr:
        return False

    return True


def _extract_json_array(text: str) -> list:
    """Kuloodporne wyciąganie JSONa z odpowiedzi LLM."""
    start = text.find('[')
    end = text.rfind(']')
    
    if start != -1 and end != -1 and end > start:
        json_str = text[start:end+1]
        try:
            # Próbujemy załadować czysty wycinek
            return json.loads(json_str)
        except json.JSONDecodeError:
            # Jeśli model wygenerował niedomknięte cudzysłowy, ignorujemy
            return []
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
        
        # Pętla generująca
        while len(current) < instr_per_topic and attempts < max_attempts_per_topic:
            need = instr_per_topic - len(current)
            request_n = min(10, need)
            temperature = random.choice(INSTRUCTION_TEMPERATURES)
            
            prompt = INSTRUCTIONS_PROMPT_TEMPLATE.format(topic=topic, n=request_n)

            if no_new_attempts >= 3:
                prompt = (
                    f"Topic: '{topic}'.\n"
                    f"Generate {need} direct beginner-friendly Python coding instructions for this topic.\n"
                    "Do not ask questions, do not explain, and do not philosophize.\n"
                    "Start each item with a command verb and output only a JSON array of strings. Nothing else."
                )

            text = ollama_generate(prompt, temperature)
            attempts += 1
            
            if not text:
                no_new_attempts += 1
                continue

            candidates = _extract_json_array(text)
            new_count = 0
            
            for cand in candidates:
                cand = str(cand).strip()
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

        # Zapis w locie po przetworzeniu każdego tematu
        pd.DataFrame(rows).to_csv(INSTR_FILE, index=False)

    return pd.DataFrame(rows)