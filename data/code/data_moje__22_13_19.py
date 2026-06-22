import math
import string
import collections
import json

class PasswordEvaluationResult:
    def __init__(self, is_valid, entropy_bits, length, charset_size, charset_types, failure_reasons):
        self.is_valid = is_valid
        self.entropy_bits = entropy_bits
        self.length = length
        self.charset_size = charset_size
        self.charset_types = charset_types
        self.failure_reasons = failure_reasons

    def __str__(self):
        return json.dumps({
            "is_valid": self.is_valid,
            "entropy_bits": round(self.entropy_bits, 2),
            "length": self.length,
            "charset_size": self.charset_size,
            "charset_types": self.charset_types,
            "failure_reasons": self.failure_reasons
        }, indent=2)

def evaluate_password(password, min_entropy=60.0, min_length=8):
    if not password:
        return PasswordEvaluationResult(False, 0.0, 0, 0, 0, ["Password is empty"])

    length = len(password)
    types_used = 0
    charset_size = 0
    lower_case = False
    upper_case = False
    digits = False
    special = False

    for char in password:
        if char in string.ascii_lowercase:
            lower_case = True
        elif char in string.ascii_uppercase:
            upper_case = True
        elif char in string.digits:
            digits = True
        elif char in string.punctuation or char in string.whitespace:
            special = True
        else:
            special = True

    if lower_case:
        types_used += 1
        charset_size += 26
    if upper_case:
        types_used += 1
        charset_size += 26
    if digits:
        types_used += 1
        charset_size += 10
    if special:
        types_used += 1
        charset_size += 32

    if charset_size == 0:
        charset_size = 128

    entropy_bits = length * math.log2(charset_size)

    failure_reasons = []
    if entropy_bits < min_entropy:
        failure_reasons.append(f"Entropy below minimum ({entropy_bits:.2f} < {min_entropy})")
    if length < min_length:
        failure_reasons.append(f"Length below minimum ({length} < {min_length})")

    is_valid = len(failure_reasons) == 0

    return PasswordEvaluationResult(
        is_valid=is_valid,
        entropy_bits=entropy_bits,
        length=length,
        charset_size=charset_size,
        charset_types=types_used,
        failure_reasons=failure_reasons
    )

if __name__ == '__main__':
    weak_password = "abc123"
    strong_password = "Tr0ub4d0r&3x!"
    
    result_weak = evaluate_password(weak_password)
    print("Weak Password Result:")
    print(result_weak)
    
    result_strong = evaluate_password(strong_password)
    print("Strong Password Result:")
    print(result_strong)