def check_password_strength(password: str) -> dict:
    has_lower = 0
    has_upper = 0
    has_digit = 0
    has_special = 0
    
    for char in password:
        code = ord(char)
        has_lower |= 1 if (code >= 97) and (code <= 122) else 0
        has_upper |= 1 if (code >= 65) and (code <= 90) else 0
        has_digit |= 1 if (code >= 48) and (code <= 57) else 0
        has_special |= 1 if not (code == 95) and ((code < 48) or (code > 57) and (code < 65) or (code > 90) and (code < 97) or (code > 122)) else 0
    
    return {
        "lower": bool(has_lower),
        "upper": bool(has_upper),
        "digit": bool(has_digit),
        "special": bool(has_special),
        "mask": has_lower | (has_upper << 1) | (has_digit << 2) | (has_special << 3)
    }

if __name__ == '__main__':
    test_pwd = "SecureP@ss123"
    result = check_password_strength(test_pwd)
    print(result)
    test_pwd2 = "weak"
    result2 = check_password_strength(test_pwd2)
    print(result2)