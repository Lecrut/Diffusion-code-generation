def validate_credentials(username, password):
    rules = {
        'min_length_username': (username, 8),
        'min_length_password': (password, 12),
        'has_digit': any(char.isdigit() for char in password),
        'has_uppercase': any(char.isupper() for char in password),
        'has_lowercase': any(char.islower() for char in password),
        'no_username_in_password': (username.lower(), password.lower())
    }
    
    return all(
        not isinstance(value, tuple) or len(value[0]) >= value[1]
        if value[1] is not None else True
        for value in rules.values()
    ) and rules['has_digit'] and rules['has_uppercase'] and rules['has_lowercase'] and not 'username' in rules['no_username_in_password'][1]

if __name__ == '__main__':
    sample_username = 'user123'
    sample_password = 'Passw0rd!'
    print(validate_credentials(sample_username, sample_password))