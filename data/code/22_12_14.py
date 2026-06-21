import sys
import time

def check_password_strength(password: str) -> dict:
    if not password:
        return {'is_strong': False, 'length': 0, 'has_uppercase': False, 'has_lowercase': False, 'has_digit': False, 'has_special': False, 'score': 0, 'level': 'empty'}
    length = len(password)
    has_uppercase = 0
    has_lowercase = 0
    has_digit = 0
    has_special = 0
    for char in password:
        code = ord(char)
        if 65 <= code <= 90:
            has_uppercase = 1
        elif 97 <= code <= 122:
            has_lowercase = 1
        elif 48 <= code <= 57:
            has_digit = 1
        else:
            has_special = 1
    flags = has_uppercase | has_lowercase << 1 | has_digit << 2 | has_special << 3
    score = 0
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if length >= 16:
        score += 1
    if has_uppercase:
        score += 1
    if has_lowercase:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1
    is_strong = flags == 15 and length >= 12 and (score >= 5)
    if is_strong:
        level = 'strong'
    elif score >= 4:
        level = 'medium'
    elif score >= 2:
        level = 'weak'
    else:
        level = 'very_weak'
    return {'is_strong': is_strong, 'length': length, 'has_uppercase': bool(has_uppercase), 'has_lowercase': bool(has_lowercase), 'has_digit': bool(has_digit), 'has_special': bool(has_special), 'score': score, 'level': level}

def check_password_strength_bitwise(password: str) -> int:
    if not password:
        return 0
    length = len(password)
    mask = 0
    for char in password:
        code = ord(char)
        if (code >= 65) & (code <= 90):
            mask |= 1
        if (code >= 97) & (code <= 122):
            mask |= 2
        if (code >= 48) & (code <= 57):
            mask |= 4
        if not (65 <= code <= 90 or 97 <= code <= 122 or 48 <= code <= 57):
            mask |= 8
    if length >= 8:
        mask |= 16
    if length >= 12:
        mask |= 32
    if length >= 16:
        mask |= 64
    strong_mask = 255
    char_set_complete = mask & 15 == 15
    length_sufficient = mask & 32 != 0
    if char_set_complete and length_sufficient:
        mask |= 128
    return mask
if __name__ == '__main__':
    test_passwords = ['short', 'LongEnoughButNoSpecial123', 'Str0ng!Passw0rd#2024', 'abcdefghijklmnopqrstuvwxyz', 'AbCdEfGhIjKlMnOpQrStUvWxYz1234567890!@#$%^&*()', '', '12345678', 'password', 'P@ssw0rd!2024Secure']
    print('=== Detailed Password Strength Analysis ===')
    for pwd in test_passwords:
        result = check_password_strength(pwd)
        print(f'Password: {repr(pwd)}')
        print(f"  Length: {result['length']}")
        print(f"  Has Uppercase: {result['has_uppercase']}")
        print(f"  Has Lowercase: {result['has_lowercase']}")
        print(f"  Has Digit: {result['has_digit']}")
        print(f"  Has Special: {result['has_special']}")
        print(f"  Score: {result['score']}")
        print(f"  Level: {result['level']}")
        print(f"  Is Strong: {result['is_strong']}")
        print()
    print('=== Bitwise Mask Results ===')
    for pwd in test_passwords:
        mask = check_password_strength_bitwise(pwd)
        binary_mask = bin(mask)
        print(f'Password: {repr(pwd)}')
        print(f'  Mask: {mask} ({binary_mask})')
        print(f'  Uppercase: {mask & 1 != 0}')
        print(f'  Lowercase: {mask & 2 != 0}')
        print(f'  Digit: {mask & 4 != 0}')
        print(f'  Special: {mask & 8 != 0}')
        print(f'  Length >= 8: {mask & 16 != 0}')
        print(f'  Length >= 12: {mask & 32 != 0}')
        print(f'  Length >= 16: {mask & 64 != 0}')
        print(f'  Is Strong: {mask & 128 != 0}')
        print()
    print('=== Performance Benchmark ===')
    iterations = 100000
    start_time = time.perf_counter()
    for _ in range(iterations):
        check_password_strength('Str0ng!Passw0rd#2024')
    end_time = time.perf_counter()
    detailed_time = end_time - start_time
    print(f'Detailed check ({iterations} iterations): {detailed_time:.6f} seconds')
    start_time = time.perf_counter()
    for _ in range(iterations):
        check_password_strength_bitwise('Str0ng!Passw0rd#2024')
    end_time = time.perf_counter()
    bitwise_time = end_time - start_time
    print(f'Bitwise check ({iterations} iterations): {bitwise_time:.6f} seconds')
    print(f'Speedup: {detailed_time / bitwise_time:.2f}x')