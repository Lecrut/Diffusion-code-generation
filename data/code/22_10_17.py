def validate_password_strength(password: str) -> bool:
    if len(password) < 8:
        return False
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_characters = '!@#$%^&*()_+-=[]{}|;:,.<>?'
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True
        else:
            return False
    return has_upper and has_lower and has_digit and has_special

if __name__ == '__main__':
    print(validate_password_strength("Abc123!"))
    print(validate_password_strength("abc123"))
    print(validate_password_strength("ABCDEF"))
    print(validate_password_strength("12345678"))
    print(validate_password_strength("Abcdefg1!"))