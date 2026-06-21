import math
import string

def evaluate_password_entropy(password: str) -> dict:
    if not password:
        return {
            "valid": False,
            "entropy": 0.0,
            "reasons": ["Empty password"]
        }

    length = len(password)
    charset_size = 0

    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    for char in password:
        if char in string.ascii_lowercase:
            has_lower = True
        elif char in string.ascii_uppercase:
            has_upper = True
        elif char in string.digits:
            has_digit = True
        elif char in string.punctuation:
            has_special = True

    if has_lower:
        charset_size += 26
    if has_upper:
        charset_size += 26
    if has_digit:
        charset_size += 10
    if has_special:
        charset_size += 32

    if charset_size == 0:
        return {
            "valid": False,
            "entropy": 0.0,
            "reasons": ["No valid characters found"]
        }

    entropy = length * math.log2(charset_size)

    reasons = []
    if length < 8:
        reasons.append("Length less than 8")
    if not has_lower:
        reasons.append("Missing lowercase")
    if not has_upper:
        reasons.append("Missing uppercase")
    if not has_digit:
        reasons.append("Missing digit")
    if not has_special:
        reasons.append("Missing special")

    entropy_threshold = 60.0
    is_valid = length >= 8 and has_lower and has_upper and has_digit and has_special and entropy >= entropy_threshold

    if not is_valid and not reasons:
        reasons.append("Entropy too low")

    return {
        "valid": is_valid,
        "entropy": round(entropy, 4),
        "length": length,
        "charset_size": charset_size,
        "reasons": reasons
    }

if __name__ == '__main__':
    sample_passwords = [
        "short",
        "alllowercase",
        "NoNumbersHere!!",
        "StrongP@ssw0rd!"
    ]

    for pwd in sample_passwords:
        result = evaluate_password_entropy(pwd)
        print(f"{pwd}: {result}")