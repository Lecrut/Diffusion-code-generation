import math
from collections import Counter

CHARSETS = {
    'lower': 26,
    'upper': 26,
    'digit': 10,
    'special': 33,
    'space': 1,
}

MIN_ENTROPY = 60.0

def _get_charset_size(password: str) -> int:
    charset_size = 0
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    for char in password:
        if 'a' <= char <= 'z':
            has_lower = True
        elif 'A' <= char <= 'Z':
            has_upper = True
        elif '0' <= char <= '9':
            has_digit = True
        elif not char.isalnum():
            has_special = True
    if has_lower:
        charset_size += CHARSETS['lower']
    if has_upper:
        charset_size += CHARSETS['upper']
    if has_digit:
        charset_size += CHARSETS['digit']
    if has_special:
        charset_size += CHARSETS['special']
    return charset_size

def _calculate_entropy(password: str) -> float:
    if not password:
        return 0.0
    pool_size = _get_charset_size(password)
    if pool_size == 0:
        return 0.0
    length = len(password)
    entropy = length * math.log2(pool_size)
    unique_chars = len(set(password))
    if length > 1:
        entropy *= (unique_chars / length)
    return entropy

def validate_password_strength(password: str) -> bool:
    entropy = _calculate_entropy(password)
    return entropy >= MIN_ENTROPY

if __name__ == '__main__':
    samples = [
        "abc",
        "aaaaaa",
        "Passw0rd!",
        "Tr0ub4dor&3",
        "Correct Horse Battery Staple"
    ]
    for pwd in samples:
        result = validate_password_strength(pwd)
        print(result)