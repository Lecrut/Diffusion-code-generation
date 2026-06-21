from collections import Counter
from math import log2

class PasswordResult:
    def __init__(self, valid, length, entropy, diversity, reasons):
        self.valid = valid
        self.length = length
        self.entropy = entropy
        self.diversity = diversity
        self.reasons = reasons

    def __repr__(self):
        return f"PasswordResult(valid={self.valid}, length={self.length}, entropy={self.entropy:.2f}, diversity={self.diversity}, reasons={self.reasons})"

def evaluate_password_entropy(password, min_entropy=60):
    if not password:
        return PasswordResult(False, 0, 0.0, 0, ["Password cannot be empty"])
    
    length = len(password)
    char_counts = Counter(password)
    diversity = len(char_counts)
    
    charset_size = 0
    if any(c.islower() for c in password):
        charset_size += 26
    if any(c.isupper() for c in password):
        charset_size += 26
    if any(c.isdigit() for c in password):
        charset_size += 10
    if any(not c.isalnum() for c in password):
        charset_size += 32
    
    if charset_size == 0:
        entropy = 0.0
    else:
        entropy = length * log2(charset_size)
    
    reasons = []
    if entropy < min_entropy:
        reasons.append(f"Entropy {entropy:.2f} is below threshold {min_entropy}")
    if length < 8:
        reasons.append("Password length is less than 8 characters")
    if diversity < 3:
        reasons.append("Password lacks sufficient character diversity (fewer than 3 character types)")
    
    valid = len(reasons) == 0
    return PasswordResult(valid, length, entropy, diversity, reasons)

if __name__ == '__main__':
    test_passwords = [
        "abc123",
        "Password123!",
        "strongpassw0rd#2024",
        "a",
        "12345678"
    ]
    
    for pwd in test_passwords:
        result = evaluate_password_entropy(pwd)
        print(result)