import ast
import os
import random
import re
import subprocess
import sys
import tempfile
import time
import warnings
from dataclasses import dataclass

from ollama import ollama_generate

warnings.filterwarnings("ignore", category=SyntaxWarning)


CODE_TEMPERATURES = [0.15 + i * 0.05 for i in range(18)]
VALIDATE_BY_EXECUTION = os.environ.get("CODEGEN_EXECUTE_VALIDATION", "0").lower() not in {
    "0",
    "false",
    "no",
}

CODE_PROMPT_TEMPLATE = (
    "Task: {instruction}\n"
    "Return only a single complete runnable Python module.\n"
    "Include an `if __name__ == '__main__':` block with hard-coded sample values.\n"
    "Never call input(), sys.stdin, argparse required arguments, or any interactive prompt.\n"
    "The sample block must run without user input, command-line arguments, network access, or pre-existing files.\n"
    "Do not include markdown fences or prose outside the code.\n"
    "Documentation and comments are allowed only when the task explicitly asks for them."
)

CODE_START_RE = re.compile(
    r"^\s*(from\s+\S+\s+import\s+|import\s+|def\s+|async\s+def\s+|class\s+|@|if\s+__name__\s*==|[A-Za-z_]\w*\s*=)"
)
MAIN_BLOCK_RE = re.compile(r"if\s+__name__\s*==\s*(['\"])__main__\1\s*:")


@dataclass(frozen=True)
class ValidationResult:
    ok: bool
    compile_ok: bool
    runtime_ok: bool
    error: str = ""


def _extract_fenced_code(text: str) -> str:
    text = re.sub(r"<think>[\s\S]*?</think>", "", text, flags=re.IGNORECASE)
    matches = re.findall(r"```(?:python|py)?\s*([\s\S]*?)```", text, flags=re.IGNORECASE)
    if matches:
        return max(matches, key=len).strip()

    text = re.sub(r"^\s*```(?:python|py)?\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*```\s*$", "", text)
    return text.strip()


def _find_parseable_python(text: str) -> str:
    lines = text.strip().splitlines()
    if not lines:
        return ""

    start_indexes = [0]
    start_indexes.extend(i for i, line in enumerate(lines) if CODE_START_RE.match(line))
    start_indexes = list(dict.fromkeys(start_indexes))

    for start in start_indexes:
        for end in range(len(lines), start, -1):
            candidate = "\n".join(lines[start:end]).strip()
            if not candidate:
                continue
            tree, _ = _parse_source(candidate)
            if tree is not None:
                return candidate

    return text.strip()


def _clean_code_output(text: str) -> str:
    text = _extract_fenced_code(text)
    text = _find_parseable_python(text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def _ensure_main_block(text: str) -> str:
    if MAIN_BLOCK_RE.search(text):
        return text
    return f"{text}\n\nif __name__ == '__main__':\n    pass\n"


def _validation_error(exc: Exception) -> str:
    if isinstance(exc, SyntaxError):
        return f"{type(exc).__name__}: {exc.msg} at line {exc.lineno}"
    return f"{type(exc).__name__}: {exc}"


def _compile_source(code: str, file_name: str):
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always", SyntaxWarning)
        compiled = compile(code, file_name, "exec")

    syntax_warnings = [warning for warning in caught if issubclass(warning.category, SyntaxWarning)]
    if syntax_warnings:
        warning = syntax_warnings[0]
        line = getattr(warning, "lineno", None)
        if line:
            return None, f"SyntaxWarning: {warning.message} at line {line}"
        return None, f"SyntaxWarning: {warning.message}"

    return compiled, ""


def _parse_source(code: str, file_name: str = "<candidate>"):
    try:
        _, warning_error = _compile_source(code, file_name)
        if warning_error:
            return None, warning_error
        return ast.parse(code, filename=file_name), ""
    except Exception as exc:
        return None, _validation_error(exc)


def _interactive_usage_error(tree: ast.AST) -> str:
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            func = node.func
            if isinstance(func, ast.Name) and func.id == "input":
                return "interactive input() is not allowed"
            if (
                isinstance(func, ast.Attribute)
                and func.attr in {"read", "readline", "readlines"}
                and isinstance(func.value, ast.Attribute)
                and func.value.attr == "stdin"
            ):
                return "interactive sys.stdin reads are not allowed"

    return ""


def validate_code(code: str, timeout: float = 3.0, execute: bool = True) -> ValidationResult:
    if not code or not code.strip():
        return ValidationResult(False, False, False, "empty code")

    with tempfile.TemporaryDirectory(prefix="codegen_validate_") as tmp_dir:
        tmp_path = os.path.join(tmp_dir, "candidate.py")
        with open(tmp_path, "w", encoding="utf-8") as tmp_file:
            tmp_file.write(code)

        try:
            tree, parse_error = _parse_source(code, tmp_path)
            if parse_error:
                return ValidationResult(False, False, False, parse_error)
            interactive_error = _interactive_usage_error(tree)
            if interactive_error:
                return ValidationResult(False, True, False, interactive_error)
        except Exception as exc:
            return ValidationResult(False, False, False, _validation_error(exc))

        if not execute:
            return ValidationResult(True, True, False)

        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "utf-8"
        env["PYTHONWARNINGS"] = "ignore::SyntaxWarning"
        try:
            proc = subprocess.run(
                [sys.executable, "-W", "ignore::SyntaxWarning", tmp_path],
                input="",
                capture_output=True,
                cwd=tmp_dir,
                env=env,
                text=True,
                timeout=timeout,
            )
        except subprocess.TimeoutExpired:
            return ValidationResult(False, True, False, f"runtime timeout after {timeout}s")
        except Exception as exc:
            return ValidationResult(False, True, False, _validation_error(exc))

        if proc.returncode != 0:
            stderr = proc.stderr.strip() or proc.stdout.strip()
            if len(stderr) > 300:
                stderr = f"{stderr[:300]}..."
            return ValidationResult(False, True, False, f"runtime rc={proc.returncode}: {stderr}")

    return ValidationResult(True, True, True)


def is_compilable(code: str) -> bool:
    return validate_code(code, execute=False).ok


def is_valid(code: str, timeout: float = 3.0) -> bool:
    start = time.time()
    result = validate_code(code, timeout=timeout, execute=VALIDATE_BY_EXECUTION)
    elapsed = time.time() - start
    if result.ok:
        print(f"[VALIDATE] OK ({elapsed:.2f}s)", flush=True)
        return True

    print(f"[VALIDATE] FAILED ({elapsed:.2f}s): {result.error}", flush=True)
    return False


def generate_code(instruction: str, temperature: float) -> str | None:
    prompt = CODE_PROMPT_TEMPLATE.format(instruction=instruction)
    seed = random.randint(1, 2_147_483_647)
    start = time.time()
    raw_output = ollama_generate(prompt, temperature, use_cache=False, seed=seed)
    elapsed = time.time() - start
    if not raw_output:
        print(f"[OLLAMA] Failed after {elapsed:.2f}s (temp={temperature:.2f})", flush=True)
        return None

    cleaned = _clean_code_output(raw_output)
    if not cleaned:
        print(f"[OLLAMA] Empty code after cleaning (temp={temperature:.2f})", flush=True)
        return None

    result = _ensure_main_block(cleaned)
    print(f"[OLLAMA] Generated in {elapsed:.2f}s (temp={temperature:.2f})", flush=True)
    return result


def normalize_variant(code_text: str) -> str | None:
    tree, _ = _parse_source(code_text)
    if tree is None:
        return None
    return ast.dump(tree, include_attributes=False)


def generate_variants(
    instruction: str,
    min_unique: int = 10,
    max_attempts: int = 100,
    max_rounds: int = 1,
    existing_keys: set[str] | None = None,
    on_variant=None,
) -> list[str]:
    seen = set(existing_keys or set())
    variants = []
    attempt_limit = max_attempts * max(1, max_rounds)

    print(f"[VARIANTS] start target={min_unique} max_attempts={attempt_limit}", flush=True)

    for attempt in range(1, attempt_limit + 1):
        if len(variants) >= min_unique:
            break

        temperature = random.choice(CODE_TEMPERATURES)
        code_text = generate_code(instruction, temperature)
        if not code_text:
            continue

        variant_key = normalize_variant(code_text)
        if not variant_key:
            print("[VARIANTS] rejected: syntax parse failed", flush=True)
            continue

        if variant_key in seen:
            print("[VARIANTS] rejected: duplicate", flush=True)
            continue

        if not is_valid(code_text):
            continue

        seen.add(variant_key)
        variants.append(code_text)
        if on_variant is not None:
            on_variant(code_text, len(variants) - 1)
        print(f"[VARIANTS] {len(variants)}/{min_unique} after attempt={attempt}", flush=True)

    print(f"[VARIANTS] done found={len(variants)}/{min_unique}", flush=True)
    return variants
