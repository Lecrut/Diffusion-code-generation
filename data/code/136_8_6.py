def is_valid_username(username):
    return len(username) >= 8

def is_valid_password(password):
    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    no_username_in_password = username.lower() not in password.lower()
    return len(password) >= 12 and has_digit and has_upper and has_lower and no_username_in_password

def validate_credentials(username, password):
    if not is_valid_username(username):
        return False
    if not is_valid_password(password):
        return False
    return True

if __name__ == '__main__':
    sample_username = 'user123'
    sample_password = 'Passw0rd!'
    print(validate_credentials(sample_username, sample_password))