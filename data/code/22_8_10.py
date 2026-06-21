import re
import string

COMMON_PASSWORDS = [
    "password", "123456", "12345678", "qwerty", "abc123", "monkey", "master",
    "dragon", "111111", "baseball", "iloveyou", "trustno1", "sunshine", "letmein",
    "football", "shadow", "superman", "michael", "ninja", "mustang", "p assword",
    "passw0rd", "p@ssw0rd", "admin", "welcome", "hello", "charlie", "donald",
    "password1", "qwerty123", "1234567890", "123456789", "0987654321", "123123",
    "654321", "121212", "666666", "696969", "777777", "888888", "1234", "12345",
    "1234567", "123456789", "987654321", "112233", "131313", "7654321", "987654321",
    "george", "ashley", "joanna", "access", "flower", "hottie", "loveme", "4321",
    "loveme2", "pepper", "daniel", "hammer", "silver", "jennifer", "hunter", "2000",
    "angel", "biteme", "freedom", "computer", "thomas", "jessica", "pebble", "pierre",
    "marlboro", "kimberly", "gemini", "lover", "rangers", "rachel", "6969", "2112",
    "1313", "zxcvbn", "222222", "333333", "101010", "123321", "555555", "88888888",
    "anthony", "jasmine", "matthew", "232323", "999999", "1111", "12345678910", "98765432",
    "654321", "321321", "123123123", "666666666", "121212121", "5555", "1234567890a",
    "qwe123", "q1w2e3", "aaaaaa", "pass123", "1q2w3e", "qwertyuiop", "1qaz2wsx",
    "zaq1xsw2", "1q2w3e4r", "qazxsw", "asd123", "1q2w3e4r5t", "qweasdzxc",
    "123qwe", "qwerty1", "asdfgh", "1qaz2wsx3edc", "zxc123", "q1w2e3r4", "1234qwer",
    "123456a", "1234567891", "asdfghjkl", "1q2w3e4r5", "qwertyui", "123456789123456",
    "asdfasdf", "zxcvbnm", "qwerty1234", "1234567890q", "qazwsx", "1234qwe",
    "12345678a", "123456789012345", "1234567890123456", "12345678901234567",
    "123456789012345678", "1234567890123456789", "12345678901234567890"
]

MIN_LENGTH = 8

def validate_password_strength(password: str) -> dict:
    result = {
        "is_valid": True,
        "errors": []
    }

    if len(password) < MIN_LENGTH:
        result["is_valid"] = False
        result["errors"].append(f"Password must be at least {MIN_LENGTH} characters long.")

    if not re.search(r"[A-Z]", password):
        result["is_valid"] = False
        result["errors"].append("Password must contain at least one uppercase letter.")

    if not re.search(r"[a-z]", password):
        result["is_valid"] = False
        result["errors"].append("Password must contain at least one lowercase letter.")

    if not re.search(r"[0-9]", password):
        result["is_valid"] = False
        result["errors"].append("Password must contain at least one digit.")

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        result["is_valid"] = False
        result["errors"].append("Password must contain at least one special character.")

    lower_pwd = password.lower()
    for word in COMMON_PASSWORDS:
        if word in lower_pwd:
            result["is_valid"] = False
            result["errors"].append(f"Password contains a common dictionary word: '{word}'.")
            break

    if password in COMMON_PASSWORDS:
        result["is_valid"] = False
        result["errors"].append("Password is too common.")

    return result

if __name__ == '__main__':
    samples = ["short", "AllUpperNoNumNoSpecial1", "lowercasenonumber123!", "MyP@ssw0rd!", "password123"]
    for p in samples:
        print(f"{p}: {validate_password_strength(p)}")