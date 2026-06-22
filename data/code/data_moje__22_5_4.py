def validate_password(password, username, email_domain):
    if not password or len(password) < 8:
        return False
    if not username and not email_domain:
        return True
    lower_password = password.lower()
    if username:
        lower_username = username.lower()
        if lower_username in lower_password:
            return False
    if email_domain:
        lower_domain = email_domain.lower()
        if lower_domain in lower_password:
            return False
    return True

if __name__ == '__main__':
    username = "john.doe"
    email_domain = "example.com"
    password_valid = "MyS3cur3P@ss!"
    password_invalid = "john.doe123"
    password_invalid2 = "password@example.com"
    print(validate_password(password_valid, username, email_domain))
    print(validate_password(password_invalid, username, email_domain))
    print(validate_password(password_invalid2, username, email_domain))
    print(validate_password("short", username, email_domain))
    print(validate_password("12345678", username, email_domain))