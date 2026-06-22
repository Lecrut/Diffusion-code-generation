import math
import string

def calculate_entropy(password):
    if not password:
        return 0.0

    length = len(password)
    charset_size = 0
    has_lower = any(c in string.ascii_lowercase for c in password)
    has_upper = any(c in string.ascii_uppercase for c in password)
    has_digit = any(c in string.digits for c in password)
    has_special = any(c in string.punctuation for c in password)

    if has_lower:
        charset_size += 26
    if has_upper:
        charset_size += 26
    if has_digit:
        charset_size += 10
    if has_special:
        charset_size += 32

    if charset_size == 0:
        return 0.0

    entropy = length * math.log2(charset_size)
    return entropy

def is_strong_password(password, threshold=60.0):
    if not isinstance(password, str):
        return False
    entropy = calculate_entropy(password)
    return entropy >= threshold

if __name__ == '__main__':
    test_passwords = [
        "12345",
        "password",
        "P@ssw0rd!",
        "Tr0ub4dor&3",
        "correct-horse-battery-staple",
        "a" * 20,
        "A1!a"
    ]

    for pwd in test_passwords:
        ent = calculate_entropy(pwd)
        strong = is_strong_password(pwd)
        print(f"Password: {repr(pwd)}, Entropy: {ent:.2f}, Strong: {strong}")