import math
import re
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

def evaluate_password_entropy(password, min_entropy_threshold=60):
    reasons = []
    length = len(password)
    char_classes = []
    if re.search(r"[a-z]", password):
        char_classes.append(26)
    if re.search(r"[A-Z]", password):
        char_classes.append(26)
    if re.search(r"\d", password):
        char_classes.append(10)
    if re.search(r"[^a-zA-Z0-9]", password):
        char_classes.append(32)
    
    pool_size = 0
    if len(char_classes) > 0:
        pool_size = sum(char_classes)
    
    if length == 0:
        diversity = 0
        entropy = 0.0
    else:
        diversity = len(char_classes)
        entropy = length * math.log2(pool_size) if pool_size > 0 else 0.0
    
    if length < 8:
        reasons.append("Password length is too short")
    if diversity < 2:
        reasons.append("Password lacks character diversity")
    if entropy < min_entropy_threshold:
        reasons.append(f"Entropy {entropy:.2f} is below threshold {min_entropy_threshold}")
    
    is_valid = len(reasons) == 0
    return PasswordEntropyResult(is_valid, entropy, length, diversity, reasons)

if __name__ == '__main__':
    sample_passwords = ["short", "Mixed123", "VeryLongPassword123!@#", "12345678"]
    for pwd in sample_passwords:
        result = evaluate_password_entropy(pwd, 50)
        print(result.to_dict())