COMMON_WEAK_PASSWORDS = {
    "123456", "password", "12345678", "qwerty", "abc123",
    "monkey", "1234567", "letmein", "trustno1", "dragon",
    "baseball", "iloveyou", "master", "sunshine", "ashley",
    "bailey", "shadow", "superman", "qazwsx", "123123"
}

def validate_password_strength(password):
    if not password:
        return False
    
    if len(password) < 8:
        return False
    
    if password.lower() in COMMON_WEAK_PASSWORDS:
        return False
    
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special = True
            
    if not (has_lower and has_upper and (has_digit or has_special)):
        return False
    
    for i in range(len(password) - 2):
        c1, c2, c3 = ord(password[i]), ord(password[i+1]), ord(password[i+2])
        if c2 == c1 + 1 and c3 == c2 + 1:
            return False
        if c2 == c1 - 1 and c3 == c2 - 1:
            return False
            
    for i in range(len(password) - 3):
        c1, c2 = ord(password[i]), ord(password[i+1])
        c3, c4 = ord(password[i+2]), ord(password[i+3])
        if c1 == c2 == c3 == c4:
            return False
            
    return True

if __name__ == "__main__":
    test_cases = [
        "SecureP@ssw0rd",
        "password123",
        "abcdefgh",
        "MyStr0ng!",
        "123456",
        "Qwerty!@#",
        "aaabbbbcccc"
    ]
    
    results = []
    for pwd in test_cases:
        results.append((pwd, validate_password_strength(pwd)))
        
    for pwd, is_valid in results:
        print(f"{pwd}: {is_valid}")