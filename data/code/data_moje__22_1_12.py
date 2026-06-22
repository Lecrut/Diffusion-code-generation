import math
import re
import string

class PasswordValidator:
    def __init__(self, min_entropy=50):
        self.min_entropy = min_entropy

    def calculate_entropy(self, password):
        if not password:
            return 0
        
        charset_size = 0
        if re.search(r'[a-z]', password):
            charset_size += 26
        if re.search(r'[A-Z]', password):
            charset_size += 26
        if re.search(r'[0-9]', password):
            charset_size += 10
        if re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>/?\\|`~]', password):
            charset_size += 33
            
        if charset_size == 0:
            return 0
            
        pool_size = 0
        if len(password) > 0:
            unique_chars = len(set(password))
            pool_size = unique_chars
            if unique_chars == len(password):
                pool_size = len(password) * math.log2(charset_size)
            else:
                pool_size = len(password) * math.log2(charset_size)
        
        return pool_size

    def is_strong(self, password):
        entropy = self.calculate_entropy(password)
        return entropy >= self.min_entropy

if __name__ == '__main__':
    validator = PasswordValidator(min_entropy=50)
    test_passwords = ["password", "Tr0ub4dor&3", "correcthorsebatterystaple", "A1!zX9@bQ#"]
    for pwd in test_passwords:
        result = validator.is_strong(pwd)
        print(f"Password: {pwd}, Is Strong: {result}")