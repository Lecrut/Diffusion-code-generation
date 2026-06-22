def is_valid_password(password, username, email):
    if not password or len(password) < 8:
        return False
    password_lower = password.lower()
    username_lower = username.lower()
    if username_lower in password_lower:
        return False
    if '@' in email:
        domain = email.split('@', 1)[1].lower()
        if domain in password_lower:
            return False
    return True

if __name__ == '__main__':
    sample_user = "john_doe"
    sample_email = "john.doe@example.com"
    test_pass_1 = "MySecurePass123"
    test_pass_2 = "john_doePassword"
    test_pass_3 = "exampleDomainPass"
    result_1 = is_valid_password(test_pass_1, sample_user, sample_email)
    result_2 = is_valid_password(test_pass_2, sample_user, sample_email)
    result_3 = is_valid_password(test_pass_3, sample_user, sample_email)
    print(result_1)
    print(result_2)
    print(result_3)