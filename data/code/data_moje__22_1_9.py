import math
from typing import List
from collections import Counter

CHARSETS = {
    "lower": 26,
    "upper": 26,
    "digit": 10,
    "special": 32,
    "space": 1
}

CHARSET_MAP = {
    "lower": string.ascii_lowercase,
    "upper": string.ascii_uppercase,
    "digit": string.digits,
    "special": "!@#$%^&*()-_=+[]{}|;:,.<>?/~`"
}

MIN_ENTROPY_THRESHOLD = 60.0

def _check_charset_presence(password: str, charset_name: str) -> bool:
    if charset_name == "space":
        return " " in password
    
    chars = CHARSET_MAP[charset_name]
    for char in password:
        if char in chars:
            return True
    return False

def _calculate_pool_size(password: str) -> int:
    pool_size = 0
    
    if _check_charset_presence(password, "lower"):
        pool_size += CHARSETS["lower"]
    
    if _check_charset_presence(password, "upper"):
        pool_size += CHARSETS["upper"]
    
    if _check_charset_presence(password, "digit"):
        pool_size += CHARSETS["digit"]
    
    if _check_charset_presence(password, "special"):
        pool_size += CHARSETS["special"]
    
    return pool_size

def calculate_entropy(password: str) -> float:
    if not password:
        return 0.0
    
    pool_size = _calculate_pool_size(password)
    
    if pool_size == 0:
        return 0.0
    
    length = len(password)
    entropy = length * math.log2(pool_size)
    
    return entropy

def is_strong_password(password: str) -> bool:
    entropy = calculate_entropy(password)
    return entropy >= MIN_ENTROPY_THRESHOLD

if __name__ == "__main__":
    test_passwords = ["simple", "Pass1!", "Tr0ub4dor&3", "correct horse battery staple", "a", "Zz9!kL2#mP"]
    
    for pwd in test_passwords:
        entropy_val = calculate_entropy(pwd)
        strength_val = is_strong_password(pwd)
        print(f"Password: {pwd!r}")
        print(f"Entropy: {entropy_val:.2f}")
        print(f"Strong: {strength_val}")
        print()
        
    weak_password = "1234"
    strong_password = "MyS3cretP@ssw0rd!"
    
    print(f"Weak password strength: {is_strong_password(weak_password)}")
    print(f"Strong password strength: {is_strong_password(strong_password)}")