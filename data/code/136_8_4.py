def validate_credentials(username, password):
    min_username_length = 8
    min_password_length = 12
    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    username_in_password = username.lower() in password.lower()
    
    return (len(username) >= min_username_length and
            len(password) >= min_password_length and
            has_digit and
            has_upper and
            has_lower and
            not username_in_password)

if __name__ == '__main__':
    sample_username = 'user123'
    sample_password = 'Passw0rd!'
    
    result = validate_credentials(sample_username, sample_password)
    print(f"Username: {sample_username}, Password: {sample_password}")
    print(f"Valid: {result}")