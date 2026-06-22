def validate_password(password, username=None, email_domain=None):
    if password is None or len(password) < 8:
        return False
    if username is not None:
        lower_username = username.lower()
        if lower_username and lower_username in password.lower():
            return False
    if email_domain is not None:
        lower_domain = email_domain.lower()
        if lower_domain and lower_domain in password.lower():
            return False
    has_upper = False
    has_lower = False
    has_digit = False
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        if has_upper and has_lower and has_digit:
            break
    else:
        return False
    return True

if __name__ == '__main__':
    print(validate_password("Str0ng!Pass", "john", "example.com"))
    print(validate_password("johnStr0ng!Pass", "john", "example.com"))
    print(validate_password("Str0ng!Pass@example.com", "john", "example.com"))
    print(validate_password("weak", "john", "example.com"))