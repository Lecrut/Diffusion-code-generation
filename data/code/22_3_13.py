COMMON_PASSWORDS = {
    "password", "123456", "12345678", "qwerty", "abc123", "monkey", "master",
    "dragon", "111111", "baseball", "iloveyou", "trustno1", "sunshine",
    "princess", "football", "charlie", "shadow", "michael", "password1",
    "123456789", "admin", "letmein", "welcome", "login", "passw0rd", "hello",
    "qwerty123", "654321", "superman", "qazwsx", "123123", "000000",
    "mustang", "696969", "access", "love", "batman", "secret"
}

def check_password_strength(password: str) -> dict:
    is_compromised = password.lower() in COMMON_PASSWORDS
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
            
    score = 0
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1
        
    strength = "weak"
    if score >= 5:
        strength = "strong"
    elif score >= 3:
        strength = "medium"
        
    return {
        "valid": not is_compromised and score >= 3,
        "compromised": is_compromised,
        "strength": strength,
        "score": score
    }

if __name__ == '__main__':
    result1 = check_password_strength("password")
    print(result1)
    
    result2 = check_password_strength("Str0ng!Pass#2023")
    print(result2)
    
    result3 = check_password_strength("MyP@ssw0rd!")
    print(result3)