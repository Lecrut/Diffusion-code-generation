import re

def validate_password(password: str) -> dict:
    if not isinstance(password, str):
        return {"valid": False, "reason": "Password must be a string"}
    
    errors = []
    
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long")
    
    if len(password) > 128:
        errors.append("Password must not exceed 128 characters")
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
    
    if not has_upper:
        errors.append("Password must contain at least one uppercase letter")
    if not has_lower:
        errors.append("Password must contain at least one lowercase letter")
    if not has_digit:
        errors.append("Password must contain at least one digit")
    if not has_special:
        errors.append("Password must contain at least one special character")
    
    if re.search(r'(.)\1{3,}', password):
        errors.append("Password must not contain more than three repeating characters in a row")
    
    valid = len(errors) == 0
    return {"valid": valid, "errors": errors}

if __name__ == '__main__':
    test_passwords = [
        "Str0ng!Pass",
        "weak",
        "NoSpecial1",
        "AAAAAbbbb1!",
        "12345678",
        "Up1!low"
    ]
    
    for pwd in test_passwords:
        result = validate_password(pwd)
        print(result)