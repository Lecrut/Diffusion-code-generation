import re

def check_password_strength(password: str) -> dict:
    length = len(password)
    has_lower = bool(password.islower())
    has_upper = bool(password.isupper())
    has_digit = bool(password.isdigit())
    has_special = bool(re.search(r'[^A-Za-z0-9]', password))
    
    char_types = 0
    if has_lower:
        char_types |= 1
    if has_upper:
        char_types |= 2
    if has_digit:
        char_types |= 4
    if has_special:
        char_types |= 8
    
    score = 0
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if length >= 16:
        score += 1
    
    if char_types == 15:
        score += 4
    elif char_types == 14:
        score += 3
    elif char_types == 12:
        score += 2
    elif char_types == 8:
        score += 1
    
    strength = 'weak'
    if score >= 2:
        strength = 'moderate'
    if score >= 5:
        strength = 'strong'
    if score >= 8:
        strength = 'very_strong'
    
    return {
        'password': password,
        'length': length,
        'has_lower': has_lower,
        'has_upper': has_upper,
        'has_digit': has_digit,
        'has_special': has_special,
        'char_types': char_types,
        'score': score,
        'strength': strength
    }

if __name__ == '__main__':
    test_password = 'P@ssw0rd!2024Xy'
    result = check_password_strength(test_password)
    print(result['strength'])
    print(result['score'])
    print(result['has_special'])
    print(result['length'])