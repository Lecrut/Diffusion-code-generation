import math
import re
import string

def calculate_entropy(password: str) -> float:
    if not password:
        return 0.0
    pool_size = 0
    if re.search(r'[a-z]', password):
        pool_size += 26
    if re.search(r'[A-Z]', password):
        pool_size += 26
    if re.search(r'[0-9]', password):
        pool_size += 10
    if re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', password):
        pool_size += 32
    if pool_size == 0:
        return 0.0
    length = len(password)
    entropy = length * math.log2(pool_size)
    return entropy

def is_strong_password(password: str) -> bool:
    entropy = calculate_entropy(password)
    if entropy < 60:
        return False
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', password))
    char_types = sum([has_upper, has_lower, has_digit, has_special])
    if char_types < 3:
        return False
    return True

if __name__ == '__main__':
    test_passwords = [
        "simple",
        "Short1!",
        "WeakPass123",
        "Str0ng!P@ssw0rd",
        "VeryLongPasswordWithoutNumbersOrSpecialCharsAtAll"
    ]
    for pwd in test_passwords:
        result = is_strong_password(pwd)
        print(f"{pwd}: {result}")