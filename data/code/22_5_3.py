def validate_password(username, email, password):
    if len(password) < 8:
        return False
    
    domain = email.split('@')[-1].lower() if '@' in email else ''
    username_lower = username.lower()
    password_lower = password.lower()
    
    if username_lower in password_lower:
        return False
    
    if domain and domain in password_lower:
        return False
    
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special = True
            
    if not (has_upper and has_lower and has_digit and has_special):
        return False
        
    return True

if __name__ == '__main__':
    result = validate_password("john_doe", "john.doe@example.com", "StrongP@ss1")
    print(result)
    
    result_invalid = validate_password("john_doe", "john.doe@example.com", "weakpass")
    print(result_invalid)
    
    result_contains_user = validate_password("john_doe", "john.doe@example.com", "JohnDoeStrongP@ss1")
    print(result_contains_user)
    
    result_contains_domain = validate_password("john_doe", "john.doe@example.com", "StrongP@ss1example")
    print(result_contains_domain)