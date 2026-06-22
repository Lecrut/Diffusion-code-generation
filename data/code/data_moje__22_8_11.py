import re
import string

COMMON_PASSWORDS = {
    "password", "12345678", "123456789", "1234567890", "qwerty", "abc123",
    "monkey", "master", "dragon", "111111", "baseball", "iloveyou", "trustno1",
    "sunshine", "princess", "football", "charlie", "shadow", "michael",
    "jennifer", "hunter", "thomas", "batman", "access", "flower", "harley",
    "654321", "welcome", "maggie", "letmein", "loveme", "hello", "ranger",
    "soccer", "daniel", "ninja", "mustang", "password1", "admin", "love",
    "secret", "summer", "winter", "spring", "autumn", "hello123", "test",
    "guest", "root", "admin123", "master123", "qwerty123", "changeme",
    "default", "system", "user", "login", "password123", "1234", "12345",
    "123456", "pass", "word", "passw0rd", "p@ssword", "p@ssw0rd"
}

def validate_password_strength(password: str) -> dict:
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    score = 0
    reasons = []
    
    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        reasons.append("too short")
    
    if has_upper:
        score += 1
    else:
        reasons.append("no uppercase")
        
    if has_lower:
        score += 1
    else:
        reasons.append("no lowercase")
        
    if has_digit:
        score += 1
    else:
        reasons.append("no digits")
        
    if has_special:
        score += 1
    else:
        reasons.append("no special chars")
        
    password_lower = password.lower()
    if password_lower in COMMON_PASSWORDS:
        score -= 5
        reasons.append("common password")
        
    common_patterns = [r"(.)\1{2,}", r"0123456789", r"qwertyuiop", r"asdfghjkl", r"zxcvbnm"]
    for pattern in common_patterns:
        if re.search(pattern, password_lower):
            score -= 2
            reasons.append("predictable pattern")
            break
            
    unique_chars = len(set(password))
    if unique_chars < length * 0.7:
        score -= 1
        reasons.append("low entropy")
        
    result = {
        "is_valid": score >= 3 and len(reasons) == 0,
        "score": score,
        "reasons": reasons
    }
    return result

if __name__ == '__main__':
    test_passwords = [
        "Short1!",
        "MyP@ssw0rd!",
        "password123",
        "CorrectHorseBatteryStaple",
        "AAAA1111!"
    ]
    
    for pwd in test_passwords:
        result = validate_password_strength(pwd)
        print(f"Password: '{pwd}' -> Valid: {result['is_valid']}, Score: {result['score']}")