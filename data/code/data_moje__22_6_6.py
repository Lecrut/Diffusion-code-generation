import re

def validate_password_strength(password):
    if len(password) < 8:
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    if re.search(r"(.)\1{3,}", password):
        return False
    return True

if __name__ == '__main__':
    sample_passwords = ["Abcdef1!", "Abcdef123", "Passw0rd!", "Passss0rd", "StrongP@ss1", "Weak1"]
    results = []
    for pwd in sample_passwords:
        results.append(validate_password_strength(pwd))
    print(results)