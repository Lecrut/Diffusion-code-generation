import string
import re

def is_common_password(password):
    common_passwords = {
        "password", "123456", "12345678", "qwerty", "abc123", "monkey", "1234567", "letmein",
        "trustno1", "dragon", "baseball", "iloveyou", "master", "sunshine", "ashley",
        "bailey", "passw0rd", "shadow", "123123", "654321", "superman", "qazwsx",
        "michael", "football", "password1", "password123", "batman", "access", "thunder",
        "matrix", "love", "hockey", "ranger", "daniel", "starwars", "klaster", "mustang",
        "111111", "zxcvbnm", "000000", "pass", "test", "guest", "admin"
    }
    return password.lower() in common_passwords

def has_dictionary_words(password):
    common_words = {
        "password", "login", "welcome", "hello", "secret", "admin", "root", "user",
        "guest", "test", "master", "pass", "qwerty", "letmein", "shadow", "sunshine",
        "football", "baseball", "soccer", "hockey", "basketball", "superman", "batman",
        "spiderman", "dragon", "princess", "angel", "baby", "love", "star", "moon",
        "sun", "sky", "cloud", "rain", "snow", "ice", "fire", "water", "earth",
        "wind", "air", "light", "dark", "night", "day", "morning", "evening", "night",
        "computer", "laptop", "phone", "mobile", "tablet", "internet", "web", "site",
        "page", "link", "click", "button", "menu", "file", "folder", "document",
        "image", "picture", "photo", "video", "audio", "music", "sound", "voice",
        "text", "word", "letter", "number", "digit", "character", "symbol", "key",
        "code", "password", "username", "login", "sign", "in", "out", "up", "down",
        "left", "right", "top", "bottom", "center", "middle", "side", "edge", "corner"
    }
    cleaned = re.sub(r'[^a-zA-Z]', '', password).lower()
    for word in common_words:
        if word in cleaned and len(word) >= 4:
            return True
    return False

def validate_password_strength(password):
    if len(password) < 8:
        return {"valid": False, "reason": "Password must be at least 8 characters long"}
    
    if not any(c.isupper() for c in password):
        return {"valid": False, "reason": "Password must contain at least one uppercase letter"}
    
    if not any(c.islower() for c in password):
        return {"valid": False, "reason": "Password must contain at least one lowercase letter"}
    
    if not any(c.isdigit() for c in password):
        return {"valid": False, "reason": "Password must contain at least one digit"}
    
    if not any(c in string.punctuation for c in password):
        return {"valid": False, "reason": "Password must contain at least one special character"}
    
    if is_common_password(password):
        return {"valid": False, "reason": "Password is a commonly used password"}
    
    if has_dictionary_words(password):
        return {"valid": False, "reason": "Password contains common dictionary words"}
    
    return {"valid": True, "reason": "Password meets all strength requirements"}

if __name__ == '__main__':
    test_passwords = [
        "Short1!",
        "nouppercase1!",
        "noLowercase1!",
        "NoDigit!",
        "NoSpecial1",
        "password1!",
        "StrongP@ss1",
        "ValidPass123!"
    ]
    for pwd in test_passwords:
        print(validate_password_strength(pwd))