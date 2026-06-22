def validate_password(password, username, email):
    if not password or not username or not email:
        return False
    if username.lower() in password.lower():
        return False
    if "@" in email:
        domain = email.split("@")[1]
        if domain.lower() in password.lower():
            return False
    return True

if __name__ == '__main__':
    sample_username = "john_doe"
    sample_email = "john.doe@example.com"
    test_passwords = [
        "SecurePass123",
        "john_doeSecret",
        "MyExamplePass",
        "password123"
    ]
    for p in test_passwords:
        result = validate_password(p, sample_username, sample_email)
        print(f"Password '{p}' valid: {result}")