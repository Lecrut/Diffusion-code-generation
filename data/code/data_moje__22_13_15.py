import math
import string
import collections

class PasswordEvaluationResult:
    def __init__(self, is_valid, entropy, failure_reasons):
        self.is_valid = is_valid
        self.entropy = entropy
        self.failure_reasons = failure_reasons

    def __repr__(self):
        return (
            f"PasswordEvaluationResult(is_valid={self.is_valid}, "
            f"entropy={self.entropy}, "
            f"failure_reasons={self.failure_reasons})"
        )

def evaluate_password(password, min_entropy=60.0, min_length=8, required_chargroups=3):
    if not password:
        return PasswordEvaluationResult(False, 0.0, ["Password is empty"])

    failure_reasons = []

    if len(password) < min_length:
        failure_reasons.append(f"Length {len(password)} is less than minimum {min_length}")

    unique_chars = set(password)
    if len(unique_chars) < required_chargroups:
        failure_reasons.append(f"Diversity {len(unique_chars)} is less than minimum {required_chargroups}")

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
        charset_size = 1

    entropy = len(password) * math.log2(charset_size)

    if entropy < min_entropy:
        failure_reasons.append(f"Entropy {entropy:.2f} is less than minimum {min_entropy}")

    is_valid = len(failure_reasons) == 0
    return PasswordEvaluationResult(is_valid, entropy, failure_reasons)

if __name__ == '__main__':
    sample_passwords = [
        "short",
        "correcthorsebatterystaple",
        "Passw0rd!",
        "aaaaaaaaaaaa",
        ""
    ]
    for pw in sample_passwords:
        result = evaluate_password(pw)
        print(result)