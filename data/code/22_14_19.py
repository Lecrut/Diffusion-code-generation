COMMON_WEAK_PASSWORDS = {
    "123456", "password", "12345678", "qwerty", "abc123",
    "111111", "123123", "iloveyou", "admin", "letmein"
}

def has_sequential_chars(password: str, length: int = 3) -> bool:
    if len(password) < length:
        return False
    for i in range(len(password) - length + 1):
        char_code = ord(password[i])
        if all(ord(password[j]) == char_code + (j - i) for j in range(i + 1, i + length)):
            return True
    for i in range(len(password) - length + 1):
        char_code = ord(password[i])
        if all(ord(password[j]) == char_code - (j - i) for j in range(i + 1, i + length)):
            return True
    return False

def validate_password_strength(password: str) -> dict:
    result = {
        "is_valid": False,
        "reasons": []
    }
    if len(password) < 8:
        result["reasons"].append("Password must be at least 8 characters long")
    if password.lower() in COMMON_WEAK_PASSWORDS:
        result["reasons"].append("Password is a common weak password")
    if has_sequential_chars(password):
        result["reasons"].append("Password contains sequential characters")
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    if not (has_upper and has_lower and has_digit):
        result["reasons"].append("Password must contain uppercase, lowercase, and digit characters")
    if not result["reasons"]:
        result["is_valid"] = True
    return result

if __name__ == '__main__':
    sample_passwords = ["Password1", "qwerty123", "Str0ngP@ss", "123456", "Abc123de"]
    for pwd in sample_passwords:
        validation_result = validate_password_strength(pwd)
        print(f"Password: {pwd}, Valid: {validation_result['is_valid']}, Reasons: {validation_result['reasons']}")