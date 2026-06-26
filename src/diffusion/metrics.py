from __future__ import annotations

import ast
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class AstValidityResult:
    valid_count: int
    total_count: int
    failures: tuple[str, ...]

    @property
    def rate(self) -> float:
        if self.total_count == 0:
            return 0.0
        return self.valid_count / self.total_count


class CodeParser:
    """Language-aware parser interface for generated code validity checks."""

    language: str = "unknown"

    def is_valid(self, text: str) -> tuple[bool, str | None]:
        raise NotImplementedError


class PythonAstParser(CodeParser):
    language = "python"

    def is_valid(self, text: str) -> tuple[bool, str | None]:
        try:
            ast.parse(text)
        except SyntaxError as exc:
            return False, f"{exc.__class__.__name__}: {exc.msg}"
        except Exception as exc:
            return False, f"{exc.__class__.__name__}: {exc}"
        return True, None


class PythonCompileParser(CodeParser):
    language = "python"

    def is_valid(self, text: str) -> tuple[bool, str | None]:
        try:
            compile(text, "<generated-code>", "exec")
        except SyntaxError as exc:
            return False, f"{exc.__class__.__name__}: {exc.msg}"
        except Exception as exc:
            return False, f"{exc.__class__.__name__}: {exc}"
        return True, None


def ast_validity_rate(
    generated_texts: Iterable[str],
    *,
    parser: CodeParser | None = None,
    max_failures: int = 3,
) -> AstValidityResult:
    parser = parser or PythonAstParser()
    valid_count = 0
    total_count = 0
    failures: list[str] = []

    for text in generated_texts:
        total_count += 1
        ok, error = parser.is_valid(text)
        if ok:
            valid_count += 1
        elif error is not None and len(failures) < max_failures:
            failures.append(error)

    return AstValidityResult(
        valid_count=valid_count,
        total_count=total_count,
        failures=tuple(failures),
    )


def compile_validity_rate(
    generated_texts: Iterable[str],
    *,
    parser: CodeParser | None = None,
    max_failures: int = 3,
) -> AstValidityResult:
    return ast_validity_rate(
        generated_texts,
        parser=parser or PythonCompileParser(),
        max_failures=max_failures,
    )


def levenshtein_distance(left: str, right: str) -> int:
    """Return the character-level edit distance between two strings."""
    if left == right:
        return 0
    if len(left) < len(right):
        left, right = right, left
    if not right:
        return len(left)

    previous = list(range(len(right) + 1))
    for left_idx, left_char in enumerate(left, start=1):
        current = [left_idx]
        for right_idx, right_char in enumerate(right, start=1):
            insert_cost = current[right_idx - 1] + 1
            delete_cost = previous[right_idx] + 1
            replace_cost = previous[right_idx - 1] + int(left_char != right_char)
            current.append(min(insert_cost, delete_cost, replace_cost))
        previous = current
    return previous[-1]


def normalized_levenshtein_distance(left: str, right: str) -> float:
    denominator = max(len(left), len(right), 1)
    return levenshtein_distance(left, right) / denominator
