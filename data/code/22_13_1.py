import string
import math
import json

class PasswordEntropyResult:
    def __init__(self, entropy_bits: float, length: int, char_sets_used: int, is_valid: bool, reasons: list):
        self.entropy_bits = entropy_bits
        self.length = length
        self.char_sets_used = char_sets_used
        self.is_valid = is_valid
        self.reasons = reasons

    def to_dict(self) -> dict:
        return {
            "entropy_bits": self.entropy_bits,
            "length": self.length,
            "char_sets_used": self.char_sets_used,
            "is_valid": self.is_valid,
            "reasons": self.reasons
        }

def evaluate_password_entropy(password: str, min_entropy_bits: float = 60.0, min_length: int = 8) -> PasswordEntropyResult:
    if not isinstance(password, str):
        return PasswordEntropyResult(
            entropy_bits=0.0,
            length=0,
            char_sets_used=0,
            is_valid=False,
            reasons=["Password must be a string"]
        )

    length = len(password)
    char_sets_used = 0
    pool_size = 0

    if any(c in string.ascii_lowercase for c in password):
        pool_size += 26
        char_sets_used += 1
    if any(c in string.ascii_uppercase for c in password):
        pool_size += 26
        char_sets_used += 1
    if any(c in string.digits for c in password):
        pool_size += 10
        char_sets_used += 1
    if any(c in string.punctuation for c in password):
        pool_size += len(string.punctuation)
        char_sets_used += 1

    if length == 0:
        entropy_bits = 0.0
    else:
        if pool_size > 0:
            entropy_bits = length * math.log2(pool_size)
        else:
            entropy_bits = 0.0

    reasons = []
    is_valid = True

    if length < min_length:
        reasons.append(f"Length {length} is less than minimum {min_length}")
        is_valid = False

    if entropy_bits < min_entropy_bits:
        reasons.append(f"Entropy {entropy_bits:.2f} bits is below threshold {min_entropy_bits} bits")
        is_valid = False

    if char_sets_used < 3:
        reasons.append(f"Uses only {char_sets_used} character sets, expected at least 3")
        is_valid = False

    return PasswordEntropyResult(
        entropy_bits=entropy_bits,
        length=length,
        char_sets_used=char_sets_used,
        is_valid=is_valid,
        reasons=reasons
    )

if __name__ == '__main__':
    password = "MyP@ssw0rd123!"
    result = evaluate_password_entropy(password)
    print(json.dumps(result.to_dict(), indent=2))