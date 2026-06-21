import string
import math
import enum

class PasswordEvaluationStatus(enum.Enum):
    VALID = "valid"
    TOO_SHORT = "too_short"
    TOO_SIMPLE = "too_simple"
    TOO_MONOTONOUS = "too_monotonous"

class PasswordEvaluationResult:
    def __init__(self, status: PasswordEvaluationStatus, entropy: float, details: dict):
        self.status = status
        self.entropy = entropy
        self.details = details

    def __repr__(self):
        return (
            f"PasswordEvaluationResult("
            f"status={self.status.value}, "
            f"entropy={self.entropy:.2f}, "
            f"details={self.details})"
        )

def evaluate_password_entropy(
    password: str,
    min_length: int = 8,
    min_entropy: float = 50.0,
    min_unique_chars: int = 4,
    max_repetition_ratio: float = 0.5,
) -> PasswordEvaluationResult:
    length = len(password)
    if length == 0:
        return PasswordEvaluationResult(
            PasswordEvaluationStatus.TOO_SHORT,
            0.0,
            {"reason": "empty_password", "length": 0},
        )

    charset_size = 0
    if any(c in string.ascii_lowercase for c in password):
        charset_size += 26
    if any(c in string.ascii_uppercase for c in password):
        charset_size += 26
    if any(c in string.digits for c in password):
        charset_size += 10
    if any(c in string.punctuation for c in password):
        charset_size += 32

    if charset_size == 0:
        return PasswordEvaluationResult(
            PasswordEvaluationStatus.TOO_SIMPLE,
            0.0,
            {"reason": "invalid_characters", "length": length},
        )

    entropy = length * math.log2(charset_size) if charset_size > 1 else 0.0

    if length < min_length:
        return PasswordEvaluationResult(
            PasswordEvaluationStatus.TOO_SHORT,
            entropy,
            {
                "reason": "too_short",
                "length": length,
                "min_length": min_length,
                "entropy": entropy,
            },
        )

    unique_chars = len(set(password))
    if unique_chars < min_unique_chars:
        return PasswordEvaluationResult(
            PasswordEvaluationStatus.TOO_SIMPLE,
            entropy,
            {
                "reason": "too_simple",
                "unique_chars": unique_chars,
                "min_unique_chars": min_unique_chars,
                "entropy": entropy,
            },
        )

    max_repeat = 1
    current_repeat = 1
    for i in range(1, length):
        if password[i] == password[i - 1]:
            current_repeat += 1
            if current_repeat > max_repeat:
                max_repeat = current_repeat
        else:
            current_repeat = 1

    repetition_ratio = max_repeat / length
    if repetition_ratio > max_repetition_ratio:
        return PasswordEvaluationResult(
            PasswordEvaluationStatus.TOO_MONOTONOUS,
            entropy,
            {
                "reason": "too_monotonous",
                "max_repetition": max_repeat,
                "repetition_ratio": repetition_ratio,
                "entropy": entropy,
            },
        )

    if entropy < min_entropy:
        return PasswordEvaluationResult(
            PasswordEvaluationStatus.TOO_SIMPLE,
            entropy,
            {
                "reason": "insufficient_entropy",
                "entropy": entropy,
                "min_entropy": min_entropy,
            },
        )

    return PasswordEvaluationResult(
        PasswordEvaluationStatus.VALID,
        entropy,
        {
            "reason": "accepted",
            "length": length,
            "charset_size": charset_size,
            "unique_chars": unique_chars,
            "entropy": entropy,
        },
    )

if __name__ == "__main__":
    test_passwords = [
        "abc123",
        "MyP@ssw0rd!",
        "a" * 10,
        "short",
        "Valid!Str1ng",
    ]

    for pwd in test_passwords:
        result = evaluate_password_entropy(pwd)
        print(result)