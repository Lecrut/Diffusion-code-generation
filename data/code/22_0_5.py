import re

def validate_password_strength(password: str) -> dict:
    if len(password) < 8:
        return {"valid": False, "reason": "Password must be at least 8 characters long."}
    
    if not re.search(r'[A-Z]', password):
        return {"valid": False, "reason": "Password must contain at least one uppercase letter."}
    
    if not re.search(r'[a-z]', password):
        return {"valid": False, "reason": "Password must contain at least one lowercase letter."}
    
    if not re.search(r'[0-9]', password):
        return {"valid": False, "reason": "Password must contain at least one digit."}
    
    if not re.search(r'[^A-Za-z0-9]', password):
        return {"valid": False, "reason": "Password must contain at least one special character."}
    
    return {"valid": True, "reason": "Password meets all strength requirements."}

if __name__ == '__main__':
    test_passwords = [
        "Short1!",
        "NoUpper1!",
        "noLower1!",
        "NoDigit!",
        "NoSpecial1",
        "ValidPass1!"
    ]
    
    results = []
    for pwd in test_passwords:
        results.append((pwd, validate_password_strength(pwd)))
    
    for pwd, result in results:
        print(result)