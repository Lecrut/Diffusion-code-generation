def validate_credentials(username, password):
    MIN_USERNAME_LENGTH = 8
    MIN_PASSWORD_LENGTH = 12
    REQUIRE_DIGIT = True
    REQUIRE_UPPERCASE = True
    REQUIRE_LOWERCASE = True

    if len(username) < MIN_USERNAME_LENGTH:
        raise ValueError("Username must be at least 8 characters long.")
    
    if len(password) < MIN_PASSWORD_LENGTH:
        raise ValueError("Password must be at least 12 characters long.")
    
    if REQUIRE_DIGIT and not any(char.isdigit() for char in password):
        raise ValueError("Password must contain at least one digit.")
    
    if REQUIRE_UPPERCASE and not any(char.isupper() for char in password):
        raise ValueError("Password must contain at least one uppercase letter.")
    
    if REQUIRE_LOWERCASE and not any(char.islower() for char in password):
        raise ValueError("Password must contain at least one lowercase letter.")
    
    if username.lower() in password.lower():
        raise ValueError("Username cannot be part of the password.")

    return True

if __name__ == '__main__':
    sample_username = 'user123'
    sample_password = 'Passw0rd!'
    try:
        print(validate_credentials(sample_username, sample_password))
    except ValueError as e:
        print(e)