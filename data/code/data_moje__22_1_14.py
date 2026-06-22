import math
import string

def calculate_entropy(password):
    if not password:
        return 0.0
    charset_size = 0
    if any(c in string.ascii_lowercase for c in password):
        charset_size += 26
    if any(c in string.ascii_uppercase for c in password):
        charset_size += 26
    if any(c in string.digits for c in password):
        charset_size += 10
    if any(c in string.punctuation for c in password):
        charset_size += 32
    if any(c in string.ascii_letters + string.digits + string.punctuation for c in password):
        remaining_chars = set(password) - set(string.ascii_letters + string.digits + string.punctuation)
        if remaining_chars:
            charset_size += len(remaining_chars)
    if charset_size == 0:
        return 0.0
    length = len(password)
    entropy = length * math.log2(charset_size)
    return entropy

def is_strong_password(password, threshold=60.0):
    entropy = calculate_entropy(password)
    return entropy >= threshold

if __name__ == '__main__':
    sample_passwords = [
        "abc",
        "Password1!",
        "P@ssw0rd!Xy9",
        "12345678",
        "H3ll0_W0rld#2023"
    ]
    for pwd in sample_passwords:
        entropy = calculate_entropy(pwd)
        strong = is_strong_password(pwd)
        print(f"{pwd}: entropy={entropy:.2f}, strong={strong}")