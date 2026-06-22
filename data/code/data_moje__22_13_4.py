import math
import string

class PasswordEntropyResult:
    def __init__(self, valid: bool, entropy: float, failure_reasons: list):
        self.valid = valid
        self.entropy = entropy
        self.failure_reasons = failure_reasons

    def __str__(self):
        status = "Valid" if self.valid else "Invalid"
        reasons_str = ", ".join(self.failure_reasons) if self.failure_reasons else "None"
        return f"Password: {status}, Entropy: {self.entropy:.2f} bits, Reasons: {reasons_str}"

    def __repr__(self):
        return (f"PasswordEntropyResult(valid={self.valid}, "
                f"entropy={self.entropy:.2f}, "
                f"failure_reasons={self.failure_reasons})")

def evaluate_password(password: str, threshold: float = 60.0) -> PasswordEntropyResult:
    if not isinstance(password, str):
        return PasswordEntropyResult(False, 0.0, ["Password must be a string"])

    failure_reasons = []
    min_length = 8
    
    if len(password) < min_length:
        failure_reasons.append(f"Too short (min {min_length} chars)")
    
    has_lower = any(c in string.ascii_lowercase for c in password)
    has_upper = any(c in string.ascii_uppercase for c in password)
    has_digit = any(c in string.digits for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    diversity_count = sum([has_lower, has_upper, has_digit, has_special])
    
    if diversity_count < 2:
        failure_reasons.append("Lack of character diversity")
    
    if len(password) == 0:
        entropy = 0.0
    else:
        pool_size = 0
        if has_lower:
            pool_size += 26
        if has_upper:
            pool_size += 26
        if has_digit:
            pool_size += 10
        if has_special:
            pool_size += 32
        
        if pool_size == 0:
            entropy = 0.0
        else:
            entropy = len(password) * math.log2(pool_size)
    
    if entropy < threshold:
        failure_reasons.append(f"Entropy below threshold ({entropy:.2f} < {threshold})")
    
    valid = len(failure_reasons) == 0
    return PasswordEntropyResult(valid, entropy, failure_reasons)

if __name__ == '__main__':
    test_cases = [
        "short",
        "StrongPass123!",
        "password",
        "AllLowercase1",
        ""
    ]
    
    for pwd in test_cases:
        result = evaluate_password(pwd)
        print(result)