import math
import string

def evaluate_password_entropy(password: str) -> dict:
    if not password:
        return {'valid': False, 'reasons': ['Password is empty'], 'entropy_bits': 0.0, 'length': 0}
    length = len(password)
    charset_size = 0
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    has_whitespace = False
    for char in password:
        if char in string.ascii_lowercase:
            has_lower = True
        elif char in string.ascii_uppercase:
            has_upper = True
        elif char in string.digits:
            has_digit = True
        elif char in string.punctuation:
            has_special = True
        elif char in string.whitespace:
            has_whitespace = True
    if has_lower:
        charset_size += 26
    if has_upper:
        charset_size += 26
    if has_digit:
        charset_size += 10
    if has_special:
        charset_size += 32
    if has_whitespace:
        charset_size += 4
    if charset_size == 0:
        charset_size = 126
    entropy_bits = length * math.log2(charset_size) if charset_size > 1 else 0
    min_length = 8
    min_entropy = 60.0
    reasons = []
    if length < min_length:
        reasons.append(f'Length too short: {length} < {min_length}')
    if entropy_bits < min_entropy:
        reasons.append(f'Entropy too low: {entropy_bits:.2f} < {min_entropy:.2f}')
    if not has_lower:
        reasons.append('Missing lowercase characters')
    if not has_upper:
        reasons.append('Missing uppercase characters')
    if not has_digit:
        reasons.append('Missing digits')
    if not has_special:
        reasons.append('Missing special characters')
    is_valid = len(reasons) == 0
    return {'valid': is_valid, 'reasons': reasons, 'entropy_bits': entropy_bits, 'length': length, 'charset_size': charset_size}
if __name__ == '__main__':
    sample_passwords = ['password123', 'Str0ng!Pass#2023', 'abc', 'AAAAAA', 'aA1!']
    for pwd in sample_passwords:
        result = evaluate_password_entropy(pwd)
        print(result)