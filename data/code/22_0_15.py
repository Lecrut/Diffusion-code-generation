import re

def validate_password_strength(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[!@#$%^&*()_+\-=\[\]{};':\\|,.<>\/?]", password):
        return False
    return True

if __name__ == "__main__":
    sample_passwords = [
        "WeakPass",
        "NoSpecialChar1!",
        "StrongP@ssw0rd",
        "Short1!",
        "AllLowercase1!"
    ]
    for pwd in sample_passwords:
        print(validate_password_strength(pwd))