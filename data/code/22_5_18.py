def validate_password(username, email_domain, password):
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(not c.isalnum() for c in password):
        return False
    if username and username.lower() in password.lower():
        return False
    if email_domain and email_domain.lower() in password.lower():
        return False
    return True

if __name__ == '__main__':
    result = validate_password("john_doe", "example.com", "SecureP@ssw0rd!")
    print(result)
    result2 = validate_password("john_doe", "example.com", "john_doe123!")
    print(result2)