def validate_credentials(username, password):
    if len(username) >= 8 and len(password) >= 8:
        if username.isalnum() and password.isalnum():
            if not any(char.isdigit() for char in username):
                return True
    return False

if __name__ == '__main__':
    print(validate_credentials('user123', 'pass456'))