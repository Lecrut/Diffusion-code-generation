import math
import string
import re

def calculate_password_strength(password):
    if not password:
        return False

    length = len(password)
    
    charset_size = 0
    has_lower = bool(re.search(r'[a-z]', password))
    has_upper = bool(re.search(r'[A-Z]', password))
    has_digits = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[^a-zA-Z0-9]', password))
    
    if has_lower:
        charset_size += 26
    if has_upper:
        charset_size += 26
    if has_digits:
        charset_size += 10
    if has_special:
        charset_size += 32
    
    if charset_size == 0:
        return False
        
    entropy = length * math.log2(charset_size)
    
    return entropy >= 60

if __name__ == '__main__':
    samples = [
        "password",
        "Password1",
        "P@ssw0rd!2023",
        "abcdefghij",
        "1234567890",
        "Ab3!xY9#kL2@",
        "short",
        "",
        "VeryLongPasswordWithNumbersAndSymbols!123"
    ]
    
    results = []
    for sample in samples:
        strength = calculate_password_strength(sample)
        results.append((sample, strength))
    
    for sample, strength in results:
        print(f"{sample}: {strength}")