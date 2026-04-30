import ast
import io
import os
import random
import re
import subprocess
import sys
import tempfile
import time
import tokenize

from ollama import ollama_generate

CODE_TEMPERATURES = [i * 0.05 for i in range(11)]

CODE_PROMPT_TEMPLATE = (
    "Task: {instruction}\n"
    "Return only runnable Python code.\n"
    "Include an `if __name__ == '__main__':` block.\n"
    "Use hard-coded sample values instead of interactive input.\n"
    "No comments, docstrings, markdown, or explanation."
)


def _remove_comments(text: str) -> str:
    tokens = []
    reader = io.StringIO(text).readline
    try:
        for token in tokenize.generate_tokens(reader):
            if token.type != tokenize.COMMENT:
                tokens.append(token)
        return tokenize.untokenize(tokens)
    except tokenize.TokenError:
        return text


def _clean_code_output(text: str) -> str:
    text = re.sub(r"^```[a-zA-Z]*\n", "", text, flags=re.MULTILINE)
    text = re.sub(r"^```\s*$", "", text, flags=re.MULTILINE)
    text = re.sub(r'"""[\s\S]*?"""', '', text)
    text = re.sub(r"'''[\s\S]*?'''", '', text)
    text = _remove_comments(text)
    text = re.sub(r"\n\s*\n", "\n", text)
    return text.strip()


def _ensure_main_block(text: str) -> str:
    if "if __name__ == '__main__':" in text:
        return text
    return text + "\n\nif __name__ == '__main__':\n  raise EnvironmentError('No skip for testing')\n"


def is_valid(code: str, timeout: float = 3.0) -> bool:
    with tempfile.NamedTemporaryFile("w", suffix=".py", encoding="utf-8", delete=False) as tmp_file:
        tmp_file.write(code)
        tmp_path = tmp_file.name

    try:
        start = time.time()
        compile(code, tmp_path, "exec")
        compile_time = time.time() - start

        start = time.time()
        proc = subprocess.run([sys.executable, tmp_path], capture_output=True, timeout=timeout)
        exec_time = time.time() - start

        if proc.returncode != 0:
            print(f"[VALIDATE] FAILED (compile={compile_time:.2f}s, exec={exec_time:.2f}s, rc={proc.returncode})", flush=True)
            return False

        print(f"[VALIDATE] OK (compile={compile_time:.2f}s, exec={exec_time:.2f}s)", flush=True)
        return True
    except subprocess.TimeoutExpired:
        print(f"[VALIDATE] TIMEOUT after {timeout}s", flush=True)
        return False
    except Exception as exc:
        print(f"[VALIDATE] ERROR: {type(exc).__name__}", flush=True)
        return False
    finally:
        try:
            os.remove(tmp_path)
        except OSError:
            pass


def generate_code(instruction: str, temperature: float) -> str | None:
    prompt = CODE_PROMPT_TEMPLATE.format(instruction=instruction)
    start = time.time()
    raw_output = ollama_generate(prompt, temperature)
    elapsed = time.time() - start
    if not raw_output:
        print(f"[OLLAMA] Failed after {elapsed:.2f}s (temp={temperature:.2f})", flush=True)
        return None

    result = _ensure_main_block(_clean_code_output(raw_output))
    print(f"[OLLAMA] Generated in {elapsed:.2f}s (temp={temperature:.2f})", flush=True)
    return result


def normalize_variant(code_text: str) -> str | None:
    try:
        tree = ast.parse(code_text)
    except SyntaxError:
        return None
    return ast.dump(tree, include_attributes=False)


def generate_variants(instruction: str, min_unique: int = 10, max_attempts: int = 100, max_rounds: int = 2) -> list[str]:
    seen = set()
    variants = []
    batch_index = 0

    print(f"[VARIANTS] start target={min_unique} batch={max_attempts}", flush=True)

    for round_number in range(max_rounds):
        batch_index += 1
        print(f"[VARIANTS] batch={batch_index} have={len(variants)}/{min_unique}", flush=True)

        for _ in range(max_attempts):
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
            print(f"[VARIANTS] {len(variants)}/{min_unique}", flush=True)

            if len(variants) >= min_unique and round_number != 0:
                break
        
        if len(variants) >= min_unique:
            break

    print(f"[VARIANTS] done batches={batch_index} found={len(variants)}/{min_unique}", flush=True)
    return variants