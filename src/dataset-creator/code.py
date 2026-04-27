from ollama import ollama_generate

MAX_RETRIES = 3

CODE_PROMPT_TEMPLATE = (
    "Implement the task: {instruction}\nRequirements:\n"
    "- Return ONLY working Python code (no extra text).\n"
    "- Code must be self-contained and runnable without interactive input (no input(), no CLI args). Provide example usage via a hard-coded demo in __main__.\n"
    "- Code must be modular: split logic into functions with at least one public function having a clear name.\n"
    "- Use type hints for public functions.\n"
    "- Do NOT use magic numbers — place constants in UPPER_SNAKE_CASE.\n"
    "- Avoid global state; use parameters and return values.\n"
    "- Do not import libraries outside the Python standard library.\n"
    "- Include a short if __name__ == '__main__' block demonstrating usage with sample inputs.\n"
    "- No comments, no extra explanatory text."
)


def is_valid(code):
    try:
        exec(code, {})
        return True
    except:
        return False


def generate_code(instruction, temperature=0.6):
    prompt = CODE_PROMPT_TEMPLATE.format(instruction=instruction)
    return ollama_generate(prompt, temperature)


def generate_valid_code(instruction, max_retries=MAX_RETRIES, temperature=0.6):
    code = None
    for _ in range(max_retries):
        code = generate_code(instruction, temperature=temperature)
        if code and is_valid(code):
            return code

    return code or ""


def process_row(idx, row, max_retries=MAX_RETRIES, temperature=0.6):
    code_text = generate_valid_code(row["instruction"], max_retries=max_retries, temperature=temperature)

    return {
        "id": idx,
        "topic": row["topic"],
        "instruction": row["instruction"],
        "code": code_text,
        "valid": is_valid(code_text)
    }


def generate_variants(instruction, attempts=10, desired=3):
    """Try up to `attempts` times to generate up to `desired` unique, syntactically valid variants.

    Uniqueness is determined by AST structure (ast.dump).
    Returns list of code strings.
    """
    import ast

    seen = set()
    variants = []

    import random

    for i in range(attempts):
        # vary temperature across attempts to increase diversity;
        # keep first attempt conservative
        temp = 0.2 if i == 0 else random.uniform(0.35, 0.95)
        code_text = generate_code(instruction, temperature=temp)
        if not code_text:
            continue

        # Normalize via AST for uniqueness and syntax check
        try:
            tree = ast.parse(code_text)
            key = ast.dump(tree, include_attributes=False)
        except Exception:
            # invalid syntax
            continue

        if key in seen:
            continue

        seen.add(key)

        # Basic runtime validation: compile only (do not execute __main__ demo)
        try:
            compile(code_text, "<string>", "exec")
        except Exception:
            continue

        variants.append(code_text)
        if len(variants) >= desired:
            break

    return variants


def generate_one_fallback(instruction, extra_attempts=10):
    """If generate_variants returned nothing, attempt extra focused tries to get a single valid code."""
    for i in range(extra_attempts):
        temp = 0.2 if i == 0 else 0.5 + (i % 3) * 0.15
        code_text = generate_code(instruction, temperature=temp)
        if not code_text:
            continue
        if is_valid(code_text):
            return code_text
    return ""
