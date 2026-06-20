USERNAME_MIN_LENGTH = 8
PASSWORD_MIN_LENGTH = 12
DIGIT_THRESHOLD = 1
UPPERCASE_THRESHOLD = 1
LOWERCASE_THRESHOLD = 1

def validate_credentials(username, password):
    if len(username) < USERNAME_MIN_LENGTH:
        return False
    if len(password) < PASSWORD_MIN_LENGTH:
        return False
    if sum(char.isdigit() for char in password) < DIGIT_THRESHOLD:
        return False
    if sum(char.isupper() for char in password) < UPPERCASE_THRESHOLD:
        return False
    if sum(char.islower() for char in password) < LOWERCASE_THRESHOLD:
        return False
    if username.lower() in password.lower():
        return False
    return True

if __name__ == '__main__':
    sample_username = 'user123'
    sample_password = 'Passw0rd!'
    print(validate_credentials(sample_username, sample_password))