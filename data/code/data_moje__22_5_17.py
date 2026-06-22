def validate_password(username, email, password):
    errors = []
    if len(password) < 8:
        errors.append('Password must be at least 8 characters long.')
    if not any(c.isupper() for c in password):
        errors.append('Password must contain at least one uppercase letter.')
    if not any(c.islower() for c in password):
        errors.append('Password must contain at least one lowercase letter.')
    if not any(c.isdigit() for c in password):
        errors.append('Password must contain at least one digit.')
    if not any(not c.isalnum() for c in password):
        errors.append('Password must contain at least one special character.')
    if username and username.lower() in password.lower():
        errors.append('Password cannot contain the username.')
    if email and '@' in email:
        domain = email.split('@')[-1]
        if domain.lower() in password.lower():
            errors.append('Password cannot contain the email domain.')
    return len(errors) == 0, errors

if __name__ == '__main__':
    valid, errors = validate_password('JohnDoe', 'john.doe@company.com', 'Str0ng#Pass1')
    print(valid, errors)
    valid2, errors2 = validate_password('JohnDoe', 'john.doe@company.com', 'john')
    print(valid2, errors2)