def validate_credentials(username, password):
    if len(username) < 8:
        raise ValueError("Username must be at least 8 characters long")
    if len(password) < 12:
        raise ValueError("Password must be at least 12 characters long")
    if not any(char.isdigit() for char in password):
        raise ValueError("Password must contain at least one digit")
    if not any(char.isupper() for char in password):
        raise ValueError("Password must contain at least one uppercase letter")
    if not any(char.islower() for char in password):
        raise ValueError("Password must contain at least one lowercase letter")
    if username.lower() in password.lower():
        raise ValueError("Username should not be part of the password")
    return True

if __name__ == '__main__':
    sample_username = 'user123'
    sample_password = 'Passw0rd!'
    try:
        result = validate_credentials(sample_username, sample_password)
        print(f"Credentials valid: {result}")
    except ValueError as e:
        print(e)