import string
import re

COMMON_WEAK_PASSWORDS = {
    "password", "123456", "12345678", "qwerty", "abc123",
    "monkey", "1234567", "letmein", "trustno1", "dragon",
    "baseball", "iloveyou", "master", "sunshine", "ashley",
    "bailey", "passw0rd", "shadow", "123123", "654321"
}

def has_sequential_chars(password: str, length: int = 3) -> bool:
    if len(password) < length:
        return False
    lower_pwd = password.lower()
    for i in range(len(lower_pwd) - length + 1):
        chunk = lower_pwd[i : i + length]
        if chunk.isalpha():
            if chunk == "".join(chr(ord(chunk[j]) + 1) for j in range(len(chunk))):
                return True
        elif chunk.isdigit():
            if chunk == "".join(str(int(chunk[j]) + 1) for j in range(len(chunk))):
                return True
    return False

def validate_password_strength(password: str) -> dict:
    errors = []
    if not password:
        errors.append("Password cannot be empty")
        return {"is_valid": False, "errors": errors}

    if password.lower() in COMMON_WEAK_PASSWORDS:
        errors.append("Password is a common weak password")

    if len(password) < 8:
        errors.append("Password must be at least 8 characters long")

    if not re.search(r"[a-z]", password):
        errors.append("Password must contain a lowercase letter")

    if not re.search(r"[A-Z]", password):
        errors.append("Password must contain an uppercase letter")

    if not re.search(r"\d", password):
        errors.append("Password must contain a digit")

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        errors.append("Password must contain a special character")

    if has_sequential_chars(password):
        errors.append("Password contains sequential characters")

    return {"is_valid": len(errors) == 0, "errors": errors}

if __name__ == '__main__':
    sample_passwords = ["Password1!", "12345678", "Str0ngP@ss!", "abc123XYZ"]
    for pwd in sample_passwords:
        result = validate_password_strength(pwd)
        print(f"Password: {pwd}, Valid: {result['is_valid']}, Errors: {result['errors']}")