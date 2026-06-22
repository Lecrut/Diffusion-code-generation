import math
import string

def calculate_entropy(password):
    if not password:
        return 0.0
    char_set = set(password)
    has_lowercase = any(c in string.ascii_lowercase for c in char_set)
    has_uppercase = any(c in string.ascii_uppercase for c in char_set)
    has_digits = any(c in string.digits for c in char_set)
    has_special = any(c in string.punctuation for c in char_set)

    pool_size = 0
    if has_lowercase:
        pool_size += 26
    if has_uppercase:
        pool_size += 26
    if has_digits:
        pool_size += 10
    if has_special:
        pool_size += 32

    if pool_size == 0:
        return 0.0

    entropy = len(password) * math.log2(pool_size)
    return entropy

def is_strong_password(password, min_entropy=60):
    if not isinstance(password, str):
        return False
    entropy = calculate_entropy(password)
    return entropy >= min_entropy

if __name__ == '__main__':
    test_passwords = [
        "abc",
        "Password1!",
        "Short1!",
        "A very long password without special chars",
        "Tr0ub4d0r&3",
        "",
        "11111111",
        "CorrectHorseBatteryStaple",
        "P@ssw0rd!2024#Secure"
    ]
    for pwd in test_passwords:
        result = is_strong_password(pwd)
        print(result)