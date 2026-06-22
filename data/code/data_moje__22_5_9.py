def validate_password(password, username, email):
    if not password or not username or not email:
        return False
    password_lower = password.lower()
    username_lower = username.lower()
    if username_lower in password_lower:
        return False
    domain = ""
    if "@" in email:
        parts = email.split("@", 1)
        if len(parts) == 2:
            domain = parts[1].lower()
    if domain and domain in password_lower:
        return False
    return True

if __name__ == "__main__":
    test_username = "john_doe"
    test_email = "john.doe@example.com"
    test_password_1 = "SecurePass123"
    test_password_2 = "johnDoePass123"
    test_password_3 = "MyPass@example"
    result_1 = validate_password(test_password_1, test_username, test_email)
    result_2 = validate_password(test_password_2, test_username, test_email)
    result_3 = validate_password(test_password_3, test_username, test_email)
    print(result_1)
    print(result_2)
    print(result_3)