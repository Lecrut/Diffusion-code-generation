import re

COMMON_PASSWORDS = {
    "password", "123456", "12345678", "qwerty", "abc123", "monkey", "1234567",
    "letmein", "trustno1", "dragon", "baseball", "iloveyou", "master", "sunshine",
    "ashley", "bailey", "passw0rd", "shadow", "123123", "654321", "superman",
    "qazwsx", "michael", "football", "password1", "password123", "welcome",
    "welcome1", "admin", "login", "princess", "starwars"
}

def validate_password_strength(password: str) -> bool:
    if not isinstance(password, str) or len(password) < 8:
        return False
    
    if len(password) > 4096:
        return False
        
    if password.lower() in COMMON_PASSWORDS:
        return False
    
    pattern = r"(?:password|letmein|welcome|admin|login|qwerty|abc123|123456)"
    if re.search(pattern, password.lower()):
        return False
        
    if re.search(r".*(.)(.)\1\2", password):
        return False
        
    if re.search(r"^(.*)\1$", password):
        return False
        
    return True

if __name__ == "__main__":
    test_passwords = [
        "SecurePass1!",
        "password",
        "abcdefgh",
        "MyStr0ngP@ss",
        "12345678"
    ]
    
    for pwd in test_passwords:
        result = validate_password_strength(pwd)
        print(f"{pwd}: {result}")