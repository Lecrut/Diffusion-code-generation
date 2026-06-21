import math
import string
import json
from typing import List, Dict, Any

class PasswordEntropyResult:
    def __init__(self, is_valid: bool, entropy_bits: float, reasons: List[str], details: Dict[str, Any]):
        self.is_valid = is_valid
        self.entropy_bits = entropy_bits
        self.reasons = reasons
        self.details = details

    def to_dict(self) -> Dict[str, Any]:
        return {
            "is_valid": self.is_valid,
            "entropy_bits": round(self.entropy_bits, 2),
            "failure_reasons": self.reasons,
            "character_diversity": {
                "length": self.details["length"],
                "unique_chars": self.details["unique_chars"],
                "has_uppercase": self.details["has_uppercase"],
                "has_lowercase": self.details["has_lowercase"],
                "has_digits": self.details["has_digits"],
                "has_special": self.details["has_special"]
            },
            "pool_size": self.details["pool_size"]
        }

def evaluate_password_entropy(password: str, min_entropy: float = 50.0) -> PasswordEntropyResult:
    reasons = []
    length = len(password)
    unique_chars = len(set(password))
    
    has_upper = any(c in string.ascii_uppercase for c in password)
    has_lower = any(c in string.ascii_lowercase for c in password)
    has_digit = any(c in string.digits for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    pool_size = 0
    if has_upper:
        pool_size += 26
    if has_lower:
        pool_size += 26
    if has_digit:
        pool_size += 10
    if has_special:
        pool_size += 32
    
    if pool_size == 0:
        entropy = 0.0
    else:
        entropy = length * math.log2(pool_size) if length > 0 else 0.0
    
    if length < 8:
        reasons.append("Password length is less than 8 characters")
    
    if not has_upper:
        reasons.append("Missing uppercase letters")
    if not has_lower:
        reasons.append("Missing lowercase letters")
    if not has_digit:
        reasons.append("Missing digits")
    if not has_special:
        reasons.append("Missing special characters")
    
    if entropy < min_entropy:
        reasons.append(f"Entropy {round(entropy, 2)} bits is below the required {min_entropy} bits")
    
    is_valid = len(reasons) == 0
    
    details = {
        "length": length,
        "unique_chars": unique_chars,
        "has_uppercase": has_upper,
        "has_lowercase": has_lower,
        "has_digits": has_digit,
        "has_special": has_special,
        "pool_size": pool_size
    }
    
    return PasswordEntropyResult(is_valid, entropy, reasons, details)

if __name__ == "__main__":
    sample_password = "SecureP@ssw0rd123"
    result = evaluate_password_entropy(sample_password)
    print(json.dumps(result.to_dict(), indent=4))