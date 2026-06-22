import re
import collections

COMMON_WORDS = {
    "password", "123456", "12345678", "qwerty", "abc123", "monkey", "1234567",
    "letmein", "trustno1", "dragon", "baseball", "iloveyou", "master", "sunshine",
    "ashley", "bailey", "shadow", "superman", "qazwsx", "123123", "football",
    "password1", "password123", "welcome", "admin", "login", "princess", "starwars"
}

def is_common_word(password):
    lower_password = password.lower()
    if lower_password in COMMON_WORDS:
        return True
    for word in COMMON_WORDS:
        if len(word) <= 6:
            continue
        if word in lower_password:
            return True
    return False

def validate_password_strength(password):
    if not isinstance(password, str):
        return False
    
    if len(password) < 8:
        return False
    
    if is_common_word(password):
        return False
    
    has_letter = any(c.isalpha() for c in password)
    has_digit = any(c.isdigit() for c in password)
    
    if not (has_letter and has_digit):
        return False
    
    consecutive_chars = 0
    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            consecutive_chars += 1
    
    if consecutive_chars > 0:
        return False
        
    return True

if __name__ == '__main__':
    test_cases = [
        "Password1",
        "12345678",
        "Str0ng!Pass",
        "aaaaaaa1",
        "ValidP@ss1",
        "abc123",
        "Short1"
    ]
    
    results = []
    for pwd in test_cases:
        is_valid = validate_password_strength(pwd)
        results.append(f"{pwd}: {is_valid}")
    
    for res in results:
        print(res)