import re
import unicodedata

COMMON_WORDS = {
    "password", "passw0rd", "password1", "123456", "12345678",
    "qwerty", "abc123", "monkey", "letmein", "dragon", "master",
    "login", "admin", "welcome", "hello", "starwars", "trustno1",
    "iloveyou", "princess", "sunshine", "baseball", "soccer",
    "football", "michael", "ashley", "bailey", "shadow", "superman"
}

def normalize_text(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text).encode("ASCII", "ignore").decode("ASCII")
    return normalized.lower()

def is_common_word(password: str) -> bool:
    normalized_pass = normalize_text(password)
    if normalized_pass in COMMON_WORDS:
        return True
    for word in COMMON_WORDS:
        if len(word) >= 4 and word in normalized_pass:
            return True
    return False

def validate_password_strength(password: str) -> dict:
    results = {
        "is_valid": False,
        "length_check": False,
        "common_word_check": False,
        "errors": []
    }
    
    if len(password) < 8:
        results["errors"].append("Password must be at least 8 characters long")
    else:
        results["length_check"] = True
    
    if is_common_word(password):
        results["errors"].append("Password contains a common dictionary word")
    else:
        results["common_word_check"] = True
    
    if results["length_check"] and not results["common_word_check"]:
        results["is_valid"] = False
    elif not results["length_check"] and results["common_word_check"]:
        results["is_valid"] = False
    elif results["length_check"] and results["common_word_check"]:
        results["is_valid"] = True
    
    return results

if __name__ == '__main__':
    sample_passwords = ["Weak", "StrongPass123", "password1234", "MyS3cur3P@ss"]
    for pwd in sample_passwords:
        print(validate_password_strength(pwd))