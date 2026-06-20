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
    print(validate_credentials('user123', 'Passw0rd!'))