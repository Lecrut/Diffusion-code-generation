def validate_password(password, username=None, email=None):
    if not password or not isinstance(password, str):
        return False
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c in "!@#$%^&*()_+-=[]{}|;:',.<>?/" for c in password):
        return False
    if username and username.lower() in password.lower():
        return False
    if email:
        domain = email.split('@')[-1]
        if domain and domain.lower() in password.lower():
            return False
    return True

if __name__ == '__main__':
    print(validate_password("StrongP@ss1", "john", "john@example.com"))
    print(validate_password("john'sPass1!", "john", "john@example.com"))
    print(validate_password("ExampleDomain1!", "john", "john@example.com"))
    print(validate_password("weak1!", "john", "john@example.com"))
    print(validate_password("ValidP@ssw0rd", "john", "john@example.com"))