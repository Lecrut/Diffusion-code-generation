import math
import string

def is_strong_password(password):
    if not password:
        return False
    char_types = 0
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    for char in password:
        if char in string.ascii_uppercase:
            has_upper = True
        elif char in string.ascii_lowercase:
            has_lower = True
        elif char in string.digits:
            has_digit = True
        elif char in string.punctuation:
            has_special = True
    if has_upper:
        char_types += 1
    if has_lower:
        char_types += 1
    if has_digit:
        char_types += 1
    if has_special:
        char_types += 1
    if char_types < 3:
        return False
    if len(password) < 8:
        return False
    pool_size = 0
    if has_lower:
        pool_size += 26
    if has_upper:
        pool_size += 26
    if has_digit:
        pool_size += 10
    if has_special:
        pool_size += len(string.punctuation)
    if pool_size == 0:
        return False
    entropy = len(password) * math.log2(pool_size)
    return entropy >= 60.0

if __name__ == '__main__':
    test_passwords = [
        "weak",
        "Weak1",
        "Strong1!",
        "VeryStrong123!",
        "aA1"
    ]
    for pwd in test_passwords:
        result = is_strong_password(pwd)
        print(result)