import math
import re
import unicodedata

class PasswordStrengthValidator:
    def __init__(self, min_entropy: float = 50.0):
        self.min_entropy = min_entropy

    def calculate_entropy(self, password: str) -> float:
        if not password:
            return 0.0
        normalized_password = unicodedata.normalize('NFKC', password)
        charset_size = 0
        if re.search(r'[a-z]', normalized_password):
            charset_size += 26
        if re.search(r'[A-Z]', normalized_password):
            charset_size += 26
        if re.search(r'[0-9]', normalized_password):
            charset_size += 10
        if re.search(r'[!@#$%^&*()\-_=+[]{}|;:\'",.<>?/\\`~]', normalized_password):
            charset_size += 33
        if re.search(r'[^\x00-\x7F]', normalized_password):
            charset_size += 128
        
        if charset_size == 0:
            return 0.0
        
        length = len(normalized_password)
        return round(length * math.log2(charset_size), 2)

    def is_strong(self, password: str) -> bool:
        return self.calculate_entropy(password) >= self.min_entropy

if __name__ == '__main__':
    validator = PasswordStrengthValidator(min_entropy=50.0)
    sample_passwords = [
        "password123",
        "Tr0ub4dor&3",
        "correcthorsebatterystaple",
        "aB9!xY#2mK",
        "simple"
    ]
    for pwd in sample_passwords:
        entropy = validator.calculate_entropy(pwd)
        strength = validator.is_strong(pwd)
        print(f"Password: {pwd} | Entropy: {entropy} | Strong: {strength}")