import ast
import multiprocessing
import re
import random
from ollama import ollama_generate

CODE_TEMPERATURES = [i * 0.05 for i in range(21)]
random.shuffle(CODE_TEMPERATURES)

CODE_PROMPT_TEMPLATE = (
    "Implement the task: {instruction}\nRequirements:\n"
    "- Return ONLY working Python code. No markdown formatting blocks (do not use ```python).\n" # Wzmocniony zakaz
    "- Code must be self-contained and runnable without interactive input (no input(), no CLI args).\n"
    "- ALWAYS include an `if __name__ == '__main__':` block at the bottom, calling your functions with hard-coded, specific sample data and printing the result.\n"
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

def _run_exec(code_str, return_dict):
    try:
        exec(code_str, {"__builtins__": __builtins__}, {})
        return_dict['success'] = True
    except Exception as e:
        return_dict['success'] = False
        return_dict['error'] = str(e)

def is_valid(code, timeout=3.0):
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    return_dict['success'] = False
    
    p = multiprocessing.Process(target=_run_exec, args=(code, return_dict))
    p.start()
    p.join(timeout)
    
    if p.is_alive():
        p.terminate()
        p.join()
        return False
        
    return return_dict['success']

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

def generate_variants(instruction, attempts=15, desired=3):
    seen = set()
    variants = []
    
    for attempt in range(attempts):
        temperature = CODE_TEMPERATURES[attempt % len(CODE_TEMPERATURES)]
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
        
        if len(variants) >= desired:
            break
            
    return variants

def generate_one_fallback(instruction, extra_attempts=10):
    for attempt in range(extra_attempts):
        temperature = CODE_TEMPERATURES[attempt % len(CODE_TEMPERATURES)]
        code_text = generate_code(instruction, temperature)
        
        if code_text and is_valid(code_text):
            return code_text
    return ""