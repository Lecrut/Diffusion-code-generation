import re
import string

COMMON_PASSWORDS = frozenset([
    "password", "123456", "12345678", "qwerty", "abc123", "monkey", "letmein",
    "trustno1", "dragon", "baseball", "iloveyou", "master", "sunshine", "ashley",
    "bailey", "shadow", "superman", "qazwsx", "123123", "football", "mustang",
    "123456789", "welcome", "admin", "login", "passw0rd", "starwars", "hello",
    "charlie", "donald", "password1", "password123", "zxcvbn", "1234567890",
    "12345678901", "123456789012", "000000", "111111", "666666", "654321",
    "112233", "121212", "010203", "1q2w3e", "1q2w3e4r", "qwertyuiop"
])

DANGEROUS_SUBSTRINGS = frozenset([
    "password", "login", "admin", "user", "root", "guest", "master", "secret",
    "change", "default", "access", "system", "test", "pass", "code", "key",
    "token", "auth", "sign", "in", "out", "up", "down", "left", "right"
])

def normalize_text(text):
    normalized = text.lower()
    normalized = re.sub(r"[^a-z0-9]", "", normalized)
    return normalized

def check_dictionary_violations(password):
    normalized_pass = normalize_text(password)
    if normalized_pass in COMMON_PASSWORDS:
        return True
    for word in DANGEROUS_SUBSTRINGS:
        if len(word) >= 4 and word in normalized_pass:
            return True
    if re.search(r"\d{3,}", normalized_pass):
        return True
    if re.search(r"[a-z]{6,}", normalized_pass):
        if len(normalized_pass) <= 10:
            return True
    return False

def validate_nist_password(password):
    if not isinstance(password, str):
        return False
    if len(password) < 8:
        return False
    if len(password) > 4096:
        return False
    if check_dictionary_violations(password):
        return False
    return True

class PasswordValidator:
    def __init__(self):
        self.results = []

    def validate(self, password):
        is_valid = validate_nist_password(password)
        self.results.append({"password": password, "is_valid": is_valid})
        return is_valid

    def get_last_result(self):
        if not self.results:
            return None
        return self.results[-1]

if __name__ == "__main__":
    test_cases = [
        "Short1!",
        "WeakPass123",
        "Str0ng!P@ssw0rd",
        "Tr0ub4dor&3",
        "correcthorsebatterystaple",
        "password1234",
        "MyS3cur3P@ss!"
    ]
    validator = PasswordValidator()
    for pwd in test_cases:
        validator.validate(pwd)
    
    for res in validator.results:
        print(f"{res['password']}: {res['is_valid']}")