MIN_USERNAME_LENGTH = 8
MIN_PASSWORD_LENGTH = 12

def validate_credentials(username, password):
    if len(username) < MIN_USERNAME_LENGTH:
        return False
    if len(password) < MIN_PASSWORD_LENGTH:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if username.lower() in password.lower():
        return False
    return True

if __name__ == '__main__':
    sample_username = 'user123'
    sample_password = 'Passw0rd!'
    print(validate_credentials(sample_username, sample_password))