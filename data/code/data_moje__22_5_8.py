def validate_password(password, username, email):
    if not password or not username:
        return False
    if len(password) < 8:
        return False
    if username.lower() in password.lower():
        return False
    domain = ""
    if email and "@" in email:
        parts = email.split("@")
        if len(parts) == 2 and parts[1]:
            domain = parts[1].lower()
    if domain and domain in password.lower():
        return False
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = set("!@#$%^&*()_+-=[]{}|;:,.<>?/~`")
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True
        if has_upper and has_lower and has_digit and has_special:
            break
    if not (has_upper and has_lower and has_digit and has_special):
        return False
    return True

if __name__ == '__main__':
    sample_username = "john_doe"
    sample_email = "john@example.com"
    sample_passwords = [
        "JohnDoe123!example",
        "SecureP@ssw0rd!",
        "weakpassword",
        "Short1!",
        "NoudserName123!",
        "NoDomain123!",
        "ValidP@ss9xyz",
    ]
    for pwd in sample_passwords:
        result = validate_password(pwd, sample_username, sample_email)
        print(f"Password '{pwd}': {result}")