import ast
import os
import re
import random
import subprocess
import sys
import tempfile
import time
import py_compile
from ollama import ollama_generate

CODE_TEMPERATURES = [i * 0.05 for i in range(21)]
random.shuffle(CODE_TEMPERATURES)

CODE_PROMPT_TEMPLATE = (
    "Implement the task: {instruction}\nRequirements:\n"
    "- Return ONLY working Python code. No markdown formatting blocks (do not use ```python).\n" # Wzmocniony zakaz
    "- Code must be self-contained and runnable without interactive input (no input(), no CLI args).\n"
    "- ALWAYS include an `if __name__ == '__main__':` block at the bottom, calling your functions with hard-coded, specific sample data and printing the result.\n"
    "- Use concise variable names and concise print output: prefer result, area, value, count, output, total. Do not print long descriptions, story text, or labels such as 'history of the world:'.\n"
    "- Code must be modular: split logic into functions with at least one public function having a clear name.\n"
    "- Use type hints for public functions.\n"
    "- Do NOT use magic numbers — place constants in UPPER_SNAKE_CASE.\n"
    "- Avoid global state; use parameters and return values.\n"
    "- Actively use the Python standard library (e.g., math, datetime, itertools) if it helps.\n"
    "- Do NOT import third-party libraries (no pandas, numpy, etc.).\n"
    "- No comments, no docstrings, no extra explanatory text."
)

def _clean_code_output(text: str) -> str:
    text = re.sub(r"^```[a-zA-Z]*\n", "", text, flags=re.MULTILINE)
    text = re.sub(r"^```\s*$", "", text, flags=re.MULTILINE)
    return text.strip()

def is_valid(code, timeout=3.0):
    with tempfile.NamedTemporaryFile("w", suffix=".py", encoding="utf-8", delete=False) as tmp_file:
        tmp_file.write(code)
        tmp_path = tmp_file.name

    try:
        py_compile.compile(tmp_path, doraise=True)
        proc = subprocess.run([sys.executable, tmp_path], capture_output=True, timeout=timeout)
        return proc.returncode == 0
    except Exception:
        return False
    finally:
        try:
            os.remove(tmp_path)
        except OSError:
            pass

def generate_code(instruction, temperature):
    prompt = CODE_PROMPT_TEMPLATE.format(instruction=instruction)
    raw_output = ollama_generate(prompt, temperature)
    if raw_output:
        return _clean_code_output(raw_output)
    return None

def normalize_variant(code_text):
    try:
        tree = ast.parse(code_text)
        return ast.dump(tree, include_attributes=False)
    except Exception:
        return None

def generate_variants(instruction, min_unique=10, max_attempts=100, max_rounds=3):
    seen = set()
    variants = []
    round_count = 0

    while len(variants) < min_unique:
        round_count += 1
        for attempt in range(max_attempts):
            temperature = random.choice(CODE_TEMPERATURES)
            code_text = generate_code(instruction, temperature)

            if not code_text:
                continue

            variant_key = normalize_variant(code_text)
            if not variant_key or variant_key in seen:
                continue

            if not is_valid(code_text):
                continue

            seen.add(variant_key)
            variants.append(code_text)

        if len(variants) >= min_unique:
            break

        if max_rounds is not None and round_count >= max_rounds:
            break

    return variants

def generate_one_fallback(instruction, extra_attempts=5, max_seconds=60):
    start_time = time.monotonic()
    first_raw = None
    for attempt in range(extra_attempts):
        if time.monotonic() - start_time > max_seconds:
            break
        temperature = CODE_TEMPERATURES[attempt % len(CODE_TEMPERATURES)]
        code_text = generate_code(instruction, temperature)
        
        if not code_text:
            continue
        if first_raw is None:
            first_raw = code_text
        if is_valid(code_text):
            return code_text
    return first_raw or ""