import re

COMMON_WEAK_PASSWORDS = {
    "password", "123456", "12345678", "qwerty", "abc123",
    "monkey", "1234567", "letmein", "trustno1", "dragon",
    "baseball", "iloveyou", "master", "sunshine", "ashley",
    "bailey", "shadow", "123123", "654321", "superman"
}

def is_sequential_chars(password: str) -> bool:
    if len(password) < 3:
        return False
    for i in range(len(password) - 2):
        if ord(password[i]) + 1 == ord(password[i + 1]) and ord(password[i + 1]) + 1 == ord(password[i + 2]):
            return True
        if ord(password[i]) - 1 == ord(password[i + 1]) and ord(password[i + 1]) - 1 == ord(password[i + 2]):
            return True
    return False

def validate_password_strength(password: str) -> dict:
    result = {
        "is_valid": False,
        "errors": []
    }

    if password.lower() in COMMON_WEAK_PASSWORDS:
        result["errors"].append("Password is too common")

    if len(password) < 8:
        result["errors"].append("Password must be at least 8 characters long")

    if not re.search(r"[a-z]", password):
        result["errors"].append("Password must contain a lowercase letter")

    if not re.search(r"[A-Z]", password):
        result["errors"].append("Password must contain an uppercase letter")

    if not re.search(r"\d", password):
        result["errors"].append("Password must contain a digit")

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        result["errors"].append("Password must contain a special character")

    if is_sequential_chars(password):
        result["errors"].append("Password contains sequential characters")

    if not result["errors"]:
        result["is_valid"] = True

    return result

if __name__ == "__main__":
    sample_passwords = ["SecurePass1!", "password", "abc123XYZ!", "P@ssw0rd", "Abcdef1!", "MyStr0ngP@ss"]
    for pwd in sample_passwords:
        validation_result = validate_password_strength(pwd)
        print(f"Password: {pwd} -> Valid: {validation_result['is_valid']}, Errors: {validation_result['errors']}")