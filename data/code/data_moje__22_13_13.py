import math
import string
import collections

class PasswordResult:
    def __init__(self, is_valid: bool, entropy: float, reasons: list):
        self.is_valid = is_valid
        self.entropy = entropy
        self.reasons = reasons

    def __repr__(self):
        return (
            f"PasswordResult(is_valid={self.is_valid}, "
            f"entropy={self.entropy:.2f}, "
            f"reasons={self.reasons})"
        )

def evaluate_password(password: str, min_length: int = 8, min_entropy: float = 28.0) -> PasswordResult:
    if not password:
        return PasswordResult(False, 0.0, ["Empty password"])

    length = len(password)
    reasons = []

    if length < min_length:
        reasons.append(f"Length too short ({length} < {min_length})")

    charset_size = 0
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in password:
        if char in string.ascii_uppercase:
            has_upper = True
        elif char in string.ascii_lowercase:
            has_lower = True
        elif char in string.digits:
            has_digit = True
        elif char in string.punctuation or char in string.whitespace:
            has_special = True

    if has_upper:
        charset_size += 26
    if has_lower:
        charset_size += 26
    if has_digit:
        charset_size += 10
    if has_special:
        charset_size += 32

    if charset_size == 0:
        entropy = 0.0
        reasons.append("No recognized character classes")
    else:
        entropy = length * math.log2(charset_size)

    if entropy < min_entropy:
        reasons.append(f"Entropy too low ({entropy:.2f} < {min_entropy})")

    is_valid = length >= min_length and entropy >= min_entropy

    return PasswordResult(is_valid, entropy, reasons)

if __name__ == '__main__':
    sample_passwords = [
        "short",
        "LongEnough123!abc",
        "alllowercase",
        "",
        "Complex!Pass99#xyz",
        "NoDigitsHereaaaa",
    ]

    for pwd in sample_passwords:
        result = evaluate_password(pwd)
        print(result)