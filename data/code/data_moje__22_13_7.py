import math
import string
import json

class PasswordEntropyResult:
    def __init__(self, is_valid, entropy, length, diversity, reasons):
        self.is_valid = is_valid
        self.entropy = entropy
        self.length = length
        self.diversity = diversity
        self.reasons = reasons

    def to_dict(self):
        return {
            "is_valid": self.is_valid,
            "entropy": self.entropy,
            "length": self.length,
            "diversity": self.diversity,
            "reasons": self.reasons
        }

def evaluate_password_entropy(password, min_entropy=60, min_length=8, min_diversity=3):
    if not password:
        return PasswordEntropyResult(
            False, 0, 0, 0, ["Password is empty"]
        )

    length = len(password)
    charset_size = 0
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special = True

    if has_lower:
        charset_size += 26
    if has_upper:
        charset_size += 26
    if has_digit:
        charset_size += 10
    if has_special:
        charset_size += 33

    diversity = sum([has_lower, has_upper, has_digit, has_special])

    if length > 0 and charset_size > 0:
        entropy = length * math.log2(charset_size)
    else:
        entropy = 0.0

    reasons = []

    if entropy < min_entropy:
        reasons.append(f"Entropy {entropy:.2f} is below threshold {min_entropy}")
    if length < min_length:
        reasons.append(f"Length {length} is below minimum {min_length}")
    if diversity < min_diversity:
        reasons.append(f"Diversity {diversity} is below minimum {min_diversity}")

    is_valid = len(reasons) == 0

    return PasswordEntropyResult(is_valid, round(entropy, 2), length, diversity, reasons)

if __name__ == '__main__':
    sample_passwords = [
        "short",
        "NoNumbersOrSpecialCharsHere",
        "WeakPass1",
        "StrongP@ssw0rd123!",
        "a1B2c3D4e5F6g7H8i9J0!@#$%^&*()"
    ]

    results = []
    for pwd in sample_passwords:
        result = evaluate_password_entropy(pwd)
        results.append(result)

    for res in results:
        print(json.dumps(res.to_dict(), indent=4))