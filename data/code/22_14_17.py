import re

COMMON_WEAK_PASSWORDS = {
    "123456", "password", "123456789", "12345678", "12345", "1234567",
    "qwerty", "abc123", "111111", "123123", "1234567890", "000000",
    "iloveyou", "password1", "1234", "123456789", "sunshine", "princess"
}

def has_sequential_chars(password):
    if len(password) < 3:
        return False
    lower = password.lower()
    for i in range(len(lower) - 2):
        if ord(lower[i+1]) == ord(lower[i]) + 1 and ord(lower[i+2]) == ord(lower[i]) + 2:
            return True
    for i in range(len(lower) - 2):
        if ord(lower[i]) == ord(lower[i+1]) + 1 and ord(lower[i+2]) == ord(lower[i+1]) + 1:
            return True
    return False

def validate_password_strength(password):
    if password in COMMON_WEAK_PASSWORDS:
        return False, "Password is in the list of common weak passwords."
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if has_sequential_chars(password):
        return False, "Password contains sequential characters."
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r"\d", password):
        return False, "Password must contain at least one digit."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character."
    return True, "Password meets all strength requirements."

if __name__ == "__main__":
    test_passwords = ["Password123!", "123456", "abc12345", "StrongP@ssw0rd"]
    for pwd in test_passwords:
        is_valid, message = validate_password_strength(pwd)
        print(f"Password: {pwd} | Valid: {is_valid} | Message: {message}")