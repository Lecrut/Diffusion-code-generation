import string

def check_password_strength(password: str) -> dict:
    if not isinstance(password, str):
        return {
            "strength": 0,
            "has_upper": False,
            "has_lower": False,
            "has_digit": False,
            "has_special": False,
            "has_alpha": False,
            "is_alphanumeric": False,
            "length": 0,
            "meets_criteria": False
        }

    length = len(password)
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    has_alpha = False
    is_alphanumeric = True
    strength = 0

    upper_bits = 0
    lower_bits = 0
    digit_bits = 0
    special_bits = 0

    for char in password:
        code = ord(char)
        if 65 <= code <= 90:
            has_upper = True
            upper_bits |= (1 << (code - 65))
        elif 97 <= code <= 122:
            has_lower = True
            lower_bits |= (1 << (code - 97))
        elif 48 <= code <= 57:
            has_digit = True
            digit_bits |= (1 << (code - 48))
        else:
            has_special = True
            is_alphanumeric = False
        
        if not (65 <= code <= 90) and not (97 <= code <= 122) and not (48 <= code <= 57):
            has_alpha = False
        else:
            has_alpha = True

    if has_upper:
        strength += 1
    if has_lower:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1
    if length >= 8:
        strength += 1
    if length >= 12:
        strength += 1
    if length >= 16:
        strength += 1
    
    if not has_alpha:
        strength -= 1
    
    if strength < 0:
        strength = 0

    meets_criteria = (
        has_upper and
        has_lower and
        has_digit and
        has_special and
        length >= 8
    )

    return {
        "strength": strength,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_digit": has_digit,
        "has_special": has_special,
        "has_alpha": has_alpha,
        "is_alphanumeric": is_alphanumeric,
        "length": length,
        "meets_criteria": meets_criteria
    }

if __name__ == '__main__':
    test_password = "Complex$Pass123"
    result = check_password_strength(test_password)
    print(result)