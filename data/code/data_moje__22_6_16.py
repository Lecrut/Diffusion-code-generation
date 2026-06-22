import re

def validate_password(password: str) -> dict:
    if len(password) < 8:
        return {"valid": False, "reason": "too_short"}
    
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    if not (has_upper and has_lower and has_digit and has_special):
        return {"valid": False, "reason": "complexity_insufficient"}
    
    for i in range(len(password) - 3):
        if password[i] == password[i+1] == password[i+2] == password[i+3]:
            return {"valid": False, "reason": "too_many_repeats"}
    
    return {"valid": True, "reason": "password_strong"}

if __name__ == '__main__':
    result1 = validate_password("Short1!")
    print(result1)
    
    result2 = validate_password("no_uppercase1!")
    print(result2)
    
    result3 = validate_password("NoDigitsHere!@")
    print(result3)
    
    result4 = validate_password("111111111!")
    print(result4)
    
    result5 = validate_password("Str0ng!Pass")
    print(result5)