def validate_password_strength(password):
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    special_characters = set("!@#$%^&*()_+-=[]{}|;':\",./<>?`~")
    has_special = any(c in special_characters for c in password)
    return has_upper and has_lower and has_digit and has_special

if __name__ == '__main__':
    print(validate_password_strength("StrongP@ss1"))
    print(validate_password_strength("weakpass"))
    print(validate_password_strength("NoSpecialChar1"))
    print(validate_password_strength("NoDigits!aA"))
    print(validate_password_strength("NoUpper!1a"))
    print(validate_password_strength("NoLower!1A"))
    print(validate_password_strength("Short1!Aa"))