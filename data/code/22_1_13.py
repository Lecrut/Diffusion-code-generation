import math
import re
import string

class PasswordValidator:
    def calculate_entropy(self, password):
        if not password:
            return 0.0
        char_pool_size = 0
        if re.search(r'[a-z]', password):
            char_pool_size += 26
        if re.search(r'[A-Z]', password):
            char_pool_size += 26
        if re.search(r'[0-9]', password):
            char_pool_size += 10
        if re.search(r'[^a-zA-Z0-9]', password):
            char_pool_size += 32
        if char_pool_size == 0:
            return 0.0
        entropy = len(password) * math.log2(char_pool_size)
        return entropy

    def is_strong(self, password):
        entropy = self.calculate_entropy(password)
        if entropy < 50:
            return False
        if len(password) < 12:
            return False
        has_lower = bool(re.search(r'[a-z]', password))
        has_upper = bool(re.search(r'[A-Z]', password))
        has_digit = bool(re.search(r'[0-9]', password))
        has_special = bool(re.search(r'[^a-zA-Z0-9]', password))
        if not (has_lower and has_upper and has_digit and has_special):
            return False
        if re.search(r'(.)\1{2,}', password):
            return False
        return True

if __name__ == '__main__':
    validator = PasswordValidator()
    test_passwords = ["Weak", "Str0ng!", "CorrectHorseBatteryStaple!", "P@ssw0rd1234!"]
    for pwd in test_passwords:
        result = validator.is_strong(pwd)
        entropy = validator.calculate_entropy(pwd)
        print(f"Password: {pwd}, Strong: {result}, Entropy: {entropy:.2f} bits")