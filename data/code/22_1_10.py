import math
import string

def calculate_password_entropy(password):
    if not password:
        return 0.0
    
    length = len(password)
    
    charset_size = 0
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    
    special_characters = set(string.punctuation)
    
    for char in password:
        if char in string.ascii_lowercase:
            has_lower = True
        elif char in string.ascii_uppercase:
            has_upper = True
        elif char in string.digits:
            has_digit = True
        elif char in special_characters:
            has_special = True
    
    if has_lower:
        charset_size += 26
    if has_upper:
        charset_size += 26
    if has_digit:
        charset_size += 10
    if has_special:
        charset_size += 33
    
    if charset_size == 0:
        return 0.0
    
    entropy = length * math.log2(charset_size)
    return entropy

def is_password_strong(password, threshold=60.0):
    if not isinstance(password, str):
        return False
    entropy = calculate_password_entropy(password)
    return entropy >= threshold

if __name__ == '__main__':
    test_passwords = [
        "password",
        "P@ssw0rd!",
        "CorrectHorseBatteryStaple",
        "Tr0ub4dor&3",
        "abcdefghij",
        "A1b2C3d4E5f6G7h8",
        "!"
    ]
    
    results = {}
    for pw in test_passwords:
        entropy = calculate_password_entropy(pw)
        strong = is_password_strong(pw)
        results[pw] = {
            "entropy": entropy,
            "is_strong": strong
        }
    
    for pw, data in results.items():
        print(f"Password: {repr(pw)}")
        print(f"  Entropy: {data['entropy']:.2f} bits")
        print(f"  Is Strong: {data['is_strong']}")