def validate_credentials(username, password):
    is_valid_length = 8 <= len(username) <= 20 and 8 <= len(password) <= 20
    has_uppercase = any(char.isupper() for char in username)
    has_lowercase = any(char.islower() for char in username)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)
    is_not_common = username not in ['admin', 'user', 'guest'] and password != '123456'
    
    return all([is_valid_length, has_uppercase, has_lowercase, has_digit, has_special, is_not_common])

if __name__ == '__main__':
    print(validate_credentials('User123!', 'P@ssw0rd'))