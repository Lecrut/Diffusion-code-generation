def validate_password_strength(password):
    if not isinstance(password, str) or len(password) == 0:
        return False
    
    if len(password) < 8:
        return False
    
    has_upper = any(char.isupper() for char in password)
    if not has_upper:
        return False
    
    has_lower = any(char.islower() for char in password)
    if not has_lower:
        return False
    
    has_digit = any(char.isdigit() for char in password)
    if not has_digit:
        return False
    
    has_special = any(not char.isalnum() for char in password)
    if not has_special:
        return False
    
    consecutive_count = 1
    for i in range(1, len(password)):
        if password[i] == password[i - 1]:
            consecutive_count += 1
            if consecutive_count > 3:
                return False
        else:
            consecutive_count = 1
    
    return True

if __name__ == '__main__':
    test_cases = [
        "Abc123!!",
        "Aa1!aA1!",
        "AAAA1234",
        "StrongPass1!",
        "weak",
        "ValidStr0ng!",
        "Aa1!Aa1!Aa1!"
    ]
    
    for case in test_cases:
        result = validate_password_strength(case)
        print(f"{case}: {result}")