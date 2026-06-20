def validate_credentials(username, password):
    if len(username) < 8:
        return False
    if len(password) < 12:
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