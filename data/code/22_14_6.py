def validate_password_strength(password, common_weak_passwords=None):
    if common_weak_passwords is None:
        common_weak_passwords = ["password", "123456", "12345678", "qwerty", "abc123", "monkey", "master", "dragon", "111111", "baseball"]
    
    if not password:
        return {
            "is_strong": False,
            "errors": ["Password cannot be empty"]
        }
    
    errors = []
    
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long")
    
    if len(password) > 128:
        errors.append("Password must not exceed 128 characters")
    
    if password.lower() in common_weak_passwords:
        errors.append("Password is too common")
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    
    char_types = sum([has_upper, has_lower, has_digit, has_special])
    
    if char_types < 3:
        errors.append("Password must contain at least 3 types of characters (upper, lower, digit, special)")
    
    for i in range(len(password) - 2):
        c1 = ord(password[i])
        c2 = ord(password[i + 1])
        c3 = ord(password[i + 2])
        
        if c2 == c1 + 1 and c3 == c2 + 1:
            errors.append("Password contains sequential characters")
            break
        
        if c2 == c1 - 1 and c3 == c2 - 1:
            errors.append("Password contains sequential characters")
            break
    
    if not errors:
        return {
            "is_strong": True,
            "errors": []
        }
    else:
        return {
            "is_strong": False,
            "errors": errors
        }

if __name__ == '__main__':
    test_password = "Str0ng!Pass"
    result = validate_password_strength(test_password)
    print(result)