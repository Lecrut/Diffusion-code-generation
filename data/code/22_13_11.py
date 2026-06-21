import string
import math
from dataclasses import dataclass
from typing import List

@dataclass
class PasswordAnalysis:
    is_valid: bool
    entropy: float
    reasons: List[str]

def evaluate_password_entropy(password: str, min_length: int = 12, min_entropy: float = 50.0) -> PasswordAnalysis:
    reasons = []
    if len(password) < min_length:
        reasons.append(f"Length {len(password)} is less than required {min_length}")
    
    has_lower = any(c in string.ascii_lowercase for c in password)
    has_upper = any(c in string.ascii_uppercase for c in password)
    has_digit = any(c in string.digits for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    char_set_size = 0
    if has_lower:
        char_set_size += 26
    if has_upper:
        char_set_size += 26
    if has_digit:
        char_set_size += 10
    if has_special:
        char_set_size += 33
    
    if char_set_size < 36:
        reasons.append("Character diversity is too low")
    
    if char_set_size > 0:
        entropy = len(password) * math.log2(char_set_size)
    else:
        entropy = 0.0
        reasons.append("No valid characters found")
    
    if entropy < min_entropy:
        reasons.append(f"Entropy {entropy:.2f} is below required {min_entropy}")
    
    return PasswordAnalysis(
        is_valid=len(reasons) == 0,
        entropy=entropy,
        reasons=reasons
    )

if __name__ == '__main__':
    test_password = "MySecureP@ssw0rd123"
    result = evaluate_password_entropy(test_password, 12, 50.0)
    print(result)
    
    weak_password = "abc"
    weak_result = evaluate_password_entropy(weak_password, 12, 50.0)
    print(weak_result)