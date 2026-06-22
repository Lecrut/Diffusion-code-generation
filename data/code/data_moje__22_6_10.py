import re

def is_valid_password(password: str) -> bool:
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = bool(re.search(r'[^A-Za-z0-9]', password))
    if not (has_upper and has_lower and has_digit and has_special):
        return False
    for i in range(len(password) - 3):
        if password[i] == password[i+1] == password[i+2] == password[i+3]:
            return False
    return True

def validate_password_sample(password: str) -> dict:
    valid = is_valid_password(password)
    checks = {
        "length": len(password) >= 8,
        "has_upper": any(c.isupper() for c in password),
        "has_lower": any(c.islower() for c in password),
        "has_digit": any(c.isdigit() for c in password),
        "has_special": bool(re.search(r'[^A-Za-z0-9]', password)),
        "no_triple_repeat": not any(password[i] == password[i+1] == password[i+2] == password[i+3] for i in range(len(password) - 3))
    }
    return {
        "password": password,
        "valid": valid,
        "checks": checks
    }

if __name__ == '__main__':
    password = "Str0ng!Pass"
    result = validate_password_sample(password)
    print(result)
    
    password_weak = "weak"
    result_weak = validate_password_sample(password_weak)
    print(result_weak)
    
    password_triple = "Str0ng!aaab"
    result_triple = validate_password_sample(password_triple)
    print(result_triple)