import math
import string
import sys

class PasswordValidationResult:
    def __init__(self, is_valid, entropy, reasons):
        self.is_valid = is_valid
        self.entropy = entropy
        self.reasons = reasons

    def __repr__(self):
        return f"PasswordValidationResult(is_valid={self.is_valid}, entropy={self.entropy:.2f}, reasons={self.reasons})"

def evaluate_password_entropy(password, min_length=12, min_entropy=50):
    if not password:
        return PasswordValidationResult(False, 0, ["Password is empty"])
    
    length = len(password)
    pool_size = 0
    if any(c in string.ascii_lowercase for c in password):
        pool_size += 26
    if any(c in string.ascii_uppercase for c in password):
        pool_size += 26
    if any(c in string.digits for c in password):
        pool_size += 10
    if any(c in string.punctuation for c in password):
        pool_size += 32
    
    if pool_size == 0:
        return PasswordValidationResult(False, 0, ["Password contains no recognizable character sets"])
    
    entropy = length * math.log2(pool_size)
    reasons = []
    
    if length < min_length:
        reasons.append(f"Length {length} is below minimum {min_length}")
    
    if entropy < min_entropy:
        reasons.append(f"Entropy {entropy:.2f} is below minimum {min_entropy}")
    
    if not reasons:
        return PasswordValidationResult(True, entropy, [])
    return PasswordValidationResult(False, entropy, reasons)

if __name__ == '__main__':
    sample_passwords = [
        "short1",
        "NoNumbersOrSpecialCharsHere",
        "Str0ng!P@ssw0rd#2024",
        "a" * 20
    ]
    for pwd in sample_passwords:
        result = evaluate_password_entropy(pwd, min_length=12, min_entropy=50)
        print(result)