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
import warnings
from dataclasses import dataclass

from ollama import ollama_generate

warnings.filterwarnings("ignore", category=SyntaxWarning)


def _parse_temperature_list(value: str | None) -> list[float]:
    if not value:
        return []
    temperatures = []
    for item in value.split(","):
        try:
            temperatures.append(float(item.strip()))
        except ValueError:
            continue
    return temperatures


CODE_TEMPERATURES = _parse_temperature_list(os.environ.get("CODEGEN_TEMPERATURES")) or [
    0.0,
    0.05,
    0.1,
    0.15,
    0.2,
    0.25,
    0.3,
    0.35,
]
CODEGEN_DUPLICATE_TEMPERATURES = _parse_temperature_list(
    os.environ.get("CODEGEN_DUPLICATE_TEMPERATURES")
) or [
    0.35,
    0.45,
    0.55,
    0.65,
    0.75,
    0.85,
    0.95,
]
CODEGEN_REPAIR_TEMPERATURES = _parse_temperature_list(
    os.environ.get("CODEGEN_REPAIR_TEMPERATURES")
) or [
    0.35,
    0.45,
    0.55,
    0.65,
    0.75,
]
MAX_DUPLICATE_STREAK = int(os.environ.get("CODEGEN_MAX_DUPLICATE_STREAK", "16"))
MAX_VALIDATION_STREAK = int(os.environ.get("CODEGEN_MAX_VALIDATION_STREAK", "10"))
CODEGEN_NUM_PREDICT = int(os.environ.get("CODEGEN_NUM_PREDICT", "1024"))
VALIDATE_BY_EXECUTION = os.environ.get("CODEGEN_EXECUTE_VALIDATION", "0").lower() not in {
    "0",
    "false",
    "no",
}
SEMANTIC_VALIDATION_ENABLED = os.environ.get("CODEGEN_SEMANTIC_VALIDATION", "0").lower() not in {
    "0",
    "false",
    "no",
}

CODE_PROMPT_TEMPLATE = (
    "Task: {instruction}\n"
    "STRICT OUTPUT CONTRACT:\n"
    "1. Output only raw Python source code. No markdown fences, no prose, no explanations.\n"
    "2. Return exactly one complete runnable Python module.\n"
    "3. Include an `if __name__ == '__main__':` block with hard-coded sample values.\n"
    "4. Never call input(), sys.stdin, argparse required arguments, or any interactive prompt.\n"
    "5. The sample block must run without user input, command-line arguments, network access, or pre-existing files.\n"
    "6. The module must define the requested function or class when the task asks for one.\n"
    "7. Unless the task asks only for tests, the main block must directly call a user-defined function or instantiate/use a user-defined class.\n"
    "8. The main block must print actual returned or computed values, not a status message.\n"
    "9. For class tasks, instantiate the class inside the main block and print at least one method call result.\n"
    "10. For function tasks, call the requested function inside the main block and print its returned value.\n"
    "11. Do not only print constants, precomputed values, dictionaries, or status strings in the main block.\n"
    "12. Do not include comments beginning with # unless the task explicitly asks for comments.\n"
    "13. Do not include docstrings unless the task explicitly asks for docstrings, documentation, or explanation.\n"
    "14. Do not use placeholders, pass-only blocks, TODOs, NotImplementedError, ellipses, or demonstration-only code.\n"
    "15. The literal tokens `pass`, `NotImplementedError`, `TODO`, `...`, and `Ellipsis` must not appear anywhere in the output.\n"
    "16. Every function, class, branch, loop, and exception handler must contain real executable logic.\n"
    "17. Use clear names and simple executable code instead of comments.\n"
    "18. If the task mentions inheritance, base classes, interfaces, or generic Shape-style APIs, still write concrete executable classes and methods. Do not create abstract methods.\n"
    "19. If the task is underspecified, choose a reasonable deterministic interpretation and implement it fully instead of returning a stub.\n"
    "20. Use ValueError for unsupported concrete inputs; never use NotImplementedError.\n"
    "{variant_directive}"
    "{retry_feedback}"
)

CODE_START_RE = re.compile(
    r"^\s*(from\s+\S+\s+import\s+|import\s+|def\s+|async\s+def\s+|class\s+|@|if\s+__name__\s*==|[A-Za-z_]\w*\s*=)"
)
DOCUMENTATION_REQUEST_RE = re.compile(
    r"\b(comment(?:ed|s)?|docstring(?:s)?|document(?:ed|ation)?|well-documented|explain)\b",
    re.IGNORECASE,
)
TEST_REQUEST_RE = re.compile(r"\b(test suite|unit tests?|unittest|pytest|tests?)\b", re.IGNORECASE)
PLACEHOLDER_RE = re.compile(
    r"\b("
    r"todo|fixme|placeholder|stub|not implemented|to be implemented|"
    r"demonstration purposes|sample hardcoded|hardcoded sample|sample hard-coded|"
    r"logic moved|bypassing|simulate user input|simulating user input|"
    r"if user wants|actually|maybe|perhaps|not needed here"
    r")\b",
    re.IGNORECASE,
)
GENERIC_INSTRUCTION_WORDS = {
    "a",
    "an",
    "and",
    "accept",
    "accepted",
    "accepts",
    "arg",
    "args",
    "argument",
    "arguments",
    "best",
    "block",
    "called",
    "class",
    "clear",
    "code",
    "complete",
    "conversion",
    "converted",
    "converting",
    "development",
    "efficient",
    "ensure",
    "example",
    "follow",
    "following",
    "follows",
    "for",
    "from",
    "function",
    "given",
    "handle",
    "hard",
    "high",
    "if",
    "implement",
    "implementation",
    "in",
    "input",
    "main",
    "mathematical",
    "mathematically",
    "module",
    "named",
    "optimized",
    "practice",
    "practices",
    "program",
    "python",
    "quality",
    "return",
    "returns",
    "runnable",
    "sample",
    "script",
    "self",
    "the",
    "to",
    "use",
    "user",
    "using",
    "value",
    "values",
    "with",
    "write",
}

TERM_ALIASES = {
    "centimeter": {"centimeter", "centimeters", "cm"},
    "centimeters": {"centimeter", "centimeters", "cm"},
    "foot": {"foot", "feet", "ft"},
    "feet": {"foot", "feet", "ft"},
    "inch": {"inch", "inches"},
    "inches": {"inch", "inches"},
    "kilogram": {"kilogram", "kilograms", "kg"},
    "kilograms": {"kilogram", "kilograms", "kg"},
    "meter": {"meter", "meters", "m"},
    "meters": {"meter", "meters", "m"},
    "pound": {"pound", "pounds", "lb", "lbs"},
    "pounds": {"pound", "pounds", "lb", "lbs"},
}

VARIANT_DIRECTIVES = [
    "Use explicit helper validation before the core operation. Keep the requested public API intact.\n",
    "Use named constants for fixed conversion factors, thresholds, or repeated values. Keep the requested public API intact.\n",
    "Use a small dictionary or mapping table when the task involves lookup, categories, units, or named records. Keep the requested public API intact.\n",
    "Use clear intermediate variables and a different hard-coded sample in the main block. Keep the requested public API intact.\n",
    "Use exception-based validation for invalid inputs where appropriate. Keep the requested public API intact.\n",
    "Use a concise implementation with early returns where appropriate. Keep the requested public API intact.\n",
    "Use an object instance in the main block for class tasks, with multiple printed method-call results. Keep the requested public API intact.\n",
    "Use class constants or static helper methods when the task asks for a class. Keep the requested public API intact.\n",
]


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


def _instruction_requests_documentation(instruction: str | None) -> bool:
    return bool(instruction and DOCUMENTATION_REQUEST_RE.search(instruction))


def _instruction_requests_tests(instruction: str | None) -> bool:
    return bool(instruction and TEST_REQUEST_RE.search(instruction))


def _line_count(text: str) -> int:
    return sum(1 for line in text.splitlines() if line.strip())


def _count_comment_lines(code: str) -> int:
    try:
        tokens = tokenize.generate_tokens(io.StringIO(code).readline)
        return sum(1 for token in tokens if token.type == tokenize.COMMENT)
    except tokenize.TokenError:
        return 0


def _is_docstring_expr(node: ast.AST) -> bool:
    return (
        isinstance(node, ast.Expr)
        and isinstance(node.value, ast.Constant)
        and isinstance(node.value.value, str)
    )


def _docstring_line_count(tree: ast.AST) -> int:
    total = 0
    nodes = [tree]
    nodes.extend(
        node
        for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))
    )

    for node in nodes:
        body = getattr(node, "body", [])
        if not body or not _is_docstring_expr(body[0]):
            continue
        start = getattr(body[0], "lineno", 0) or 0
        end = getattr(body[0], "end_lineno", start) or start
        total += max(1, end - start + 1)

    return total


def _documentation_quality_error(code: str, tree: ast.AST, instruction: str | None) -> str:
    comment_lines = _count_comment_lines(code)
    docstring_lines = _docstring_line_count(tree)
    documentation_lines = comment_lines + docstring_lines
    if documentation_lines == 0:
        return ""

    total_lines = max(1, _line_count(code))
    if not _instruction_requests_documentation(instruction):
        return "comments/docstrings are not allowed unless the instruction explicitly asks for them"

    max_documentation_lines = max(4, total_lines // 5)
    if documentation_lines > max_documentation_lines:
        return (
            "too much documentation/commentary "
            f"({documentation_lines}/{total_lines} nonblank lines)"
        )

    return ""


class _DocstringStripper(ast.NodeTransformer):
    def _strip_node_docstring(self, node):
        self.generic_visit(node)
        body = getattr(node, "body", None)
        if isinstance(body, list):
            node.body = _strip_leading_docstring(body)
        return node

    visit_Module = _strip_node_docstring
    visit_FunctionDef = _strip_node_docstring
    visit_AsyncFunctionDef = _strip_node_docstring
    visit_ClassDef = _strip_node_docstring


def _strip_disallowed_documentation(code: str, instruction: str | None) -> str | None:
    if _instruction_requests_documentation(instruction):
        return None

    tree, _ = _parse_source(code)
    if tree is None:
        return None

    documentation_lines = _count_comment_lines(code) + _docstring_line_count(tree)
    if documentation_lines == 0:
        return None

    stripped_tree = _DocstringStripper().visit(tree)
    ast.fix_missing_locations(stripped_tree)
    stripped = ast.unparse(stripped_tree).strip()
    if not stripped or stripped == code.strip():
        return None
    return stripped


def _is_ellipsis_expr(node: ast.AST) -> bool:
    return (
        isinstance(node, ast.Expr)
        and isinstance(node.value, ast.Constant)
        and node.value.value is Ellipsis
    )


def _is_not_implemented_raise(node: ast.AST) -> bool:
    if not isinstance(node, ast.Raise) or node.exc is None:
        return False

    exc = node.exc
    if isinstance(exc, ast.Call):
        exc = exc.func
    return isinstance(exc, ast.Name) and exc.id == "NotImplementedError"


def _strip_leading_docstring(body: list[ast.stmt]) -> list[ast.stmt]:
    if body and _is_docstring_expr(body[0]):
        return body[1:]
    return body


def _is_placeholder_body(body: list[ast.stmt]) -> bool:
    body = _strip_leading_docstring(body)
    return not body or all(
        isinstance(statement, ast.Pass)
        or _is_ellipsis_expr(statement)
        or _is_not_implemented_raise(statement)
        for statement in body
    )


def _main_test_side(node: ast.AST) -> str | None:
    if isinstance(node, ast.Name) and node.id == "__name__":
        return "__name__"
    if isinstance(node, ast.Constant) and node.value == "__main__":
        return "__main__"
    return None


def _is_main_test(node: ast.AST) -> bool:
    if not isinstance(node, ast.Compare) or len(node.ops) != 1 or len(node.comparators) != 1:
        return False
    if not isinstance(node.ops[0], ast.Eq):
        return False

    left = _main_test_side(node.left)
    right = _main_test_side(node.comparators[0])
    return {left, right} == {"__name__", "__main__"}


def _main_blocks(tree: ast.AST) -> list[ast.If]:
    return [node for node in ast.walk(tree) if isinstance(node, ast.If) and _is_main_test(node.test)]


def _call_name(call: ast.Call) -> str | None:
    func = call.func
    if isinstance(func, ast.Name):
        return func.id
    if isinstance(func, ast.Attribute):
        return func.attr
    return None


def _top_level_definition_names(tree: ast.AST) -> set[str]:
    return {
        node.name
        for node in getattr(tree, "body", [])
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))
    }


def _top_level_class_names(tree: ast.AST) -> set[str]:
    return {node.name for node in getattr(tree, "body", []) if isinstance(node, ast.ClassDef)}


def _top_level_instance_names(tree: ast.AST, class_names: set[str]) -> set[str]:
    instances = set()
    for node in getattr(tree, "body", []):
        targets = []
        value = None
        if isinstance(node, ast.Assign):
            targets = node.targets
            value = node.value
        elif isinstance(node, ast.AnnAssign):
            targets = [node.target]
            value = node.value

        if not isinstance(value, ast.Call):
            continue
        if not isinstance(value.func, ast.Name) or value.func.id not in class_names:
            continue

        for target in targets:
            if isinstance(target, ast.Name):
                instances.add(target.id)

    return instances


def _call_exercises_definition(call: ast.Call, definitions: set[str], instances: set[str]) -> bool:
    func = call.func
    if isinstance(func, ast.Name):
        return func.id in definitions
    if isinstance(func, ast.Attribute):
        value = func.value
        if isinstance(value, ast.Name):
            return value.id in definitions or value.id in instances
    return False


def _main_block_quality_error(tree: ast.AST, instruction: str | None) -> str:
    blocks = _main_blocks(tree)
    if not blocks:
        return "missing runnable if __name__ == '__main__' sample block"

    definitions = _top_level_definition_names(tree)
    class_names = _top_level_class_names(tree)
    instances = _top_level_instance_names(tree, class_names)
    tests_requested = _instruction_requests_tests(instruction)

    for block in blocks:
        body = _strip_leading_docstring(block.body)
        if _is_placeholder_body(body):
            return "main block is empty or pass-only"

        calls = [node for statement in body for node in ast.walk(statement) if isinstance(node, ast.Call)]
        if not calls:
            return "main block does not execute any sample call"

        if definitions and not tests_requested:
            if not any(_call_exercises_definition(call, definitions, instances) for call in calls):
                return "main block does not exercise any user-defined function or class"

    return ""


def _placeholder_error(code: str, tree: ast.AST) -> str:
    match = PLACEHOLDER_RE.search(code)
    if match:
        return f"placeholder/meta commentary is not allowed: {match.group(0)!r}"

    for node in ast.walk(tree):
        if isinstance(node, ast.Pass):
            return "pass statements are not allowed in generated solutions"
        if _is_ellipsis_expr(node):
            return "ellipsis placeholders are not allowed in generated solutions"
        if _is_not_implemented_raise(node):
            return "NotImplementedError placeholders are not allowed in generated solutions"

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            if _is_placeholder_body(node.body):
                return f"{node.__class__.__name__} {node.name!r} has no implementation"

    return ""


def _defined_names(tree: ast.AST, node_types) -> set[str]:
    return {node.name for node in ast.walk(tree) if isinstance(node, node_types)}


def _required_api_error(tree: ast.AST, instruction: str | None) -> str:
    if not instruction:
        return ""

    class_names = _defined_names(tree, ast.ClassDef)
    function_names = _defined_names(tree, (ast.FunctionDef, ast.AsyncFunctionDef))

    for match in re.finditer(r"\bclass\s+(?:named|called)\s+[`'\"]?([A-Za-z_]\w*)", instruction, re.I):
        expected = match.group(1)
        if expected not in class_names:
            return f"missing requested class {expected!r}"

    for match in re.finditer(r"\bfunction\s+(?:named|called)\s+[`'\"]?([A-Za-z_]\w*)", instruction, re.I):
        expected = match.group(1)
        if expected not in function_names:
            return f"missing requested function {expected!r}"

    lowered = instruction.lower()
    if "function" in lowered and not function_names and "lambda" not in lowered:
        return "instruction asks for a function but no function is defined"
    if "class" in lowered and not class_names:
        return "instruction asks for a class but no class is defined"

    return ""


def _normalize_term(term: str) -> str:
    term = term.lower()
    if len(term) > 4 and term.endswith("ies"):
        term = f"{term[:-3]}y"
    elif len(term) > 3 and term.endswith("s"):
        term = term[:-1]
    if len(term) > 5 and term.endswith("ed"):
        term = term[:-2]
    elif len(term) > 5 and term.endswith("ing"):
        term = term[:-3]
    return term


def _text_terms(text: str) -> set[str]:
    terms = set()
    identifiers = re.findall(r"[A-Za-z][A-Za-z0-9_]*", text)
    for identifier in identifiers:
        expanded = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", identifier)
        for token in re.split(r"[^A-Za-z0-9]+|_", expanded):
            if len(token) < 2:
                continue
            normalized = _normalize_term(token)
            terms.add(normalized)
            for alias in TERM_ALIASES.get(normalized, set()):
                terms.add(_normalize_term(alias))
    return terms


def _semantic_coverage_error(code: str, instruction: str | None) -> str:
    if not SEMANTIC_VALIDATION_ENABLED:
        return ""

    if not instruction:
        return ""

    required_terms = {
        _normalize_term(token)
        for token in re.findall(r"[A-Za-z][A-Za-z0-9_]{3,}", instruction)
        if _normalize_term(token) not in GENERIC_INSTRUCTION_WORDS
    }
    if not required_terms:
        return ""

    code_words = _text_terms(code)
    covered = required_terms.intersection(code_words)
    min_covered = 1 if len(required_terms) <= 3 else 2
    if len(covered) < min_covered:
        missing = ", ".join(sorted(required_terms - covered)[:4])
        return f"code does not cover enough task-specific terms; missing examples: {missing}"

    return ""


def _quality_error(code: str, tree: ast.AST, instruction: str | None) -> str:
    for check in (
        lambda: _documentation_quality_error(code, tree, instruction),
        lambda: _placeholder_error(code, tree),
        lambda: _main_block_quality_error(tree, instruction),
        lambda: _required_api_error(tree, instruction),
        lambda: _semantic_coverage_error(code, instruction),
    ):
        error = check()
        if error:
            return error

    return ""


def validate_code(
    code: str,
    timeout: float = 3.0,
    execute: bool = True,
    instruction: str | None = None,
) -> ValidationResult:
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
            quality_error = _quality_error(code, tree, instruction)
            if quality_error:
                return ValidationResult(False, True, False, quality_error)
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


def _validate_and_report(
    code: str,
    timeout: float = 3.0,
    instruction: str | None = None,
) -> ValidationResult:
    start = time.time()
    result = validate_code(code, timeout=timeout, execute=VALIDATE_BY_EXECUTION, instruction=instruction)
    elapsed = time.time() - start
    if result.ok:
        print(f"[VALIDATE] OK ({elapsed:.2f}s)", flush=True)
    else:
        print(f"[VALIDATE] FAILED ({elapsed:.2f}s): {result.error}", flush=True)
    return result


def is_valid(code: str, timeout: float = 3.0, instruction: str | None = None) -> bool:
    return _validate_and_report(code, timeout=timeout, instruction=instruction).ok


def _retry_feedback_block(feedback: str | None) -> str:
    if not feedback:
        return ""
    return (
        "\nPREVIOUS ATTEMPT FAILED VALIDATION:\n"
        f"{feedback}\n"
        "Generate a fresh corrected module that satisfies every contract rule above.\n"
    )


def _compact_code_excerpt(code: str, max_lines: int = 18) -> str:
    lines = [line.rstrip() for line in code.strip().splitlines()]
    lines = [line for line in lines if line.strip()]
    if len(lines) > max_lines:
        return "\n".join(lines[:max_lines] + ["..."])
    return "\n".join(lines)


def _repair_feedback(error: str, code_text: str) -> str:
    guidance = []
    lowered = error.lower()
    if "pass statements" in lowered:
        guidance.append(
            "Do not use the `pass` statement anywhere. Replace every empty branch, empty function, "
            "empty class, empty except block, or stub with real executable code that returns, raises, "
            "assigns, appends, or prints a computed value."
        )
    if "placeholder" in lowered or "notimplementederror" in lowered or "ellipsis" in lowered:
        guidance.append(
            "Do not use stubs, TODOs, ellipses, placeholders, or NotImplementedError. "
            "Do not create abstract/interface-style code. Implement the requested algorithm directly "
            "with concrete return values and executable branches."
        )
    if "comments/docstrings" in lowered:
        guidance.append("Remove all comments and docstrings; use descriptive names instead.")
    if "main block" in lowered:
        guidance.append(
            "In the `if __name__ == '__main__':` block, directly call the requested function or "
            "instantiate/use the requested class and print the real result."
        )

    excerpt = _compact_code_excerpt(code_text)
    parts = [error]
    if guidance:
        parts.append("Repair requirements: " + " ".join(guidance))
    if excerpt:
        parts.append("Rejected code excerpt to avoid repeating:\n" + excerpt)
    return "\n".join(parts)


def _variant_directive_block(directive: str | None) -> str:
    if not directive:
        return ""
    return (
        "\nVARIANT DIVERSITY REQUIREMENT:\n"
        f"{directive}"
    )


def _existing_variant_block(examples: list[str] | None) -> str:
    if not examples:
        return ""

    snippets = []
    for index, example in enumerate(examples[:4], start=1):
        lines = [line.rstrip() for line in example.strip().splitlines() if line.strip()]
        snippet = "\n".join(lines[:18])
        if snippet:
            snippets.append(f"Existing variant {index}:\n{snippet}")

    if not snippets:
        return ""

    return (
        "\nAVOID COPYING THESE EXISTING VALID VARIANTS:\n"
        + "\n\n".join(snippets)
        + "\nProduce code with different structure, helper decomposition, constants, sample values, or class usage.\n"
    )


def _select_code_temperature(retry_feedback: str | None) -> float:
    if retry_feedback and retry_feedback.startswith("the previous response duplicated"):
        return random.choice(CODEGEN_DUPLICATE_TEMPERATURES)
    if retry_feedback:
        return random.choice(CODEGEN_REPAIR_TEMPERATURES)
    return random.choice(CODE_TEMPERATURES)


def generate_code(
    instruction: str,
    temperature: float,
    retry_feedback: str | None = None,
    variant_directive: str | None = None,
    existing_variant_examples: list[str] | None = None,
) -> str | None:
    prompt = CODE_PROMPT_TEMPLATE.format(
        instruction=instruction,
        variant_directive=(
            _variant_directive_block(variant_directive)
            + _existing_variant_block(existing_variant_examples)
        ),
        retry_feedback=_retry_feedback_block(retry_feedback),
    )
    seed = random.randint(1, 2_147_483_647)
    start = time.time()
    raw_output = ollama_generate(
        prompt,
        temperature,
        use_cache=False,
        seed=seed,
        num_predict=CODEGEN_NUM_PREDICT,
    )
    elapsed = time.time() - start
    if not raw_output:
        print(f"[OLLAMA] Failed after {elapsed:.2f}s (temp={temperature:.2f})", flush=True)
        return None

    cleaned = _clean_code_output(raw_output)
    if not cleaned:
        print(f"[OLLAMA] Empty code after cleaning (temp={temperature:.2f})", flush=True)
        return None

    print(f"[OLLAMA] Generated in {elapsed:.2f}s (temp={temperature:.2f})", flush=True)
    return cleaned


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
    existing_examples: list[str] | None = None,
    on_variant=None,
) -> list[str]:
    seen = set(existing_keys or set())
    variants = []
    accepted_examples = list(existing_examples or [])
    attempt_limit = max_attempts * max(1, max_rounds)
    retry_feedback = None
    duplicate_streak = 0
    duplicate_total = 0
    validation_streak = 0
    last_validation_error = None

    print(f"[VARIANTS] start target={min_unique} max_attempts={attempt_limit}", flush=True)

    for attempt in range(1, attempt_limit + 1):
        if len(variants) >= min_unique:
            break

        temperature = _select_code_temperature(retry_feedback)
        variant_directive = None
        if duplicate_streak:
            variant_directive = VARIANT_DIRECTIVES[
                (duplicate_total + len(variants)) % len(VARIANT_DIRECTIVES)
            ]
        code_text = generate_code(
            instruction,
            temperature,
            retry_feedback=retry_feedback,
            variant_directive=variant_directive,
            existing_variant_examples=accepted_examples if retry_feedback else None,
        )
        if not code_text:
            retry_feedback = "the previous response was empty or could not be cleaned into Python code"
            continue

        stripped_code = _strip_disallowed_documentation(code_text, instruction)
        if stripped_code:
            code_text = stripped_code
            print("[CLEAN] stripped disallowed comments/docstrings", flush=True)

        tree, parse_error = _parse_source(code_text)
        if tree is None:
            retry_feedback = parse_error or "syntax parse failed"
            print(f"[VARIANTS] rejected: {retry_feedback}", flush=True)
            continue
        variant_key = ast.dump(tree, include_attributes=False)

        if variant_key in seen:
            duplicate_streak += 1
            duplicate_total += 1
            validation_streak = 0
            last_validation_error = None
            next_directive = VARIANT_DIRECTIVES[
                (duplicate_total + len(variants)) % len(VARIANT_DIRECTIVES)
            ]
            retry_feedback = (
                "the previous response duplicated an existing solution. Produce a structurally different "
                "valid implementation while still satisfying the original task. "
                f"For the next attempt, {next_directive.strip()}"
            )
            print(f"[VARIANTS] rejected: duplicate streak={duplicate_streak}", flush=True)
            if duplicate_streak >= MAX_DUPLICATE_STREAK:
                print(
                    f"[VARIANTS] stopping early after {duplicate_streak} consecutive duplicates",
                    flush=True,
                )
                break
            continue

        validation = _validate_and_report(code_text, instruction=instruction)
        if not validation.ok:
            duplicate_streak = 0
            if validation.error == last_validation_error:
                validation_streak += 1
            else:
                validation_streak = 1
                last_validation_error = validation.error
            retry_feedback = _repair_feedback(validation.error, code_text)
            if validation_streak >= MAX_VALIDATION_STREAK:
                print(
                    f"[VARIANTS] stopping early after {validation_streak} consecutive validation failures: "
                    f"{validation.error}",
                    flush=True,
                )
                break
            continue

        retry_feedback = None
        duplicate_streak = 0
        validation_streak = 0
        last_validation_error = None
        seen.add(variant_key)
        variants.append(code_text)
        accepted_examples.append(code_text)
        if on_variant is not None:
            on_variant(code_text, len(variants) - 1)
        print(f"[VARIANTS] {len(variants)}/{min_unique} after attempt={attempt}", flush=True)

    print(f"[VARIANTS] done found={len(variants)}/{min_unique}", flush=True)
    return variants
