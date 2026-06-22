import math
import string
from collections import Counter

def calculate_password_strength(password: str) -> bool:
    if not password:
        return False

    length = len(password)
    if length < 8:
        return False

    charset_size = 0
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    for char in password:
        if char in string.ascii_lowercase:
            has_lower = True
        elif char in string.ascii_uppercase:
            has_upper = True
        elif char in string.digits:
            has_digit = True
        else:
            has_special = True

    if has_lower:
        charset_size += 26
    if has_upper:
        charset_size += 26
    if has_digit:
        charset_size += 10
    if has_special:
        charset_size += 32

    if charset_size == 0:
        return False

    entropy = length * math.log2(charset_size)

    if entropy < 60:
        return False

    unique_ratio = len(set(password)) / length
    if unique_ratio < 0.5:
        return False

    common_patterns = ['password', '123456', 'qwerty', 'admin', 'letmein']
    lower_pwd = password.lower()
    for pattern in common_patterns:
        if pattern in lower_pwd:
            return False

    consecutive_chars = 0
    for i in range(length - 1):
        if abs(ord(password[i]) - ord(password[i + 1])) == 1:
            consecutive_chars += 1
    
    if consecutive_chars > length / 2:
        return False

    repeated_chars_count = 0
    for char, count in Counter(password).items():
        if count >= 3:
            repeated_chars_count += count
            
    if repeated_chars_count > length / 2:
        return False

    return True

if __name__ == '__main__':
    strong_password = 'Tr0ub4dor&3!'
    weak_password = 'password123'
    print(calculate_password_strength(strong_password))
    print(calculate_password_strength(weak_password))