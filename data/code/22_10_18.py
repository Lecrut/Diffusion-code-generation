def validate_password_strength(password):
    if len(password) < 8:
        return False
    
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    special_characters = "!@#$%^&*()_+-=[]{}|;:',.<>?/"
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True
            
    return has_upper and has_lower and has_digit and has_special

if __name__ == '__main__':
    print(validate_password_strength("Abc123!x"))
    print(validate_password_strength("weak"))
    print(validate_password_strength("NOLOWERCASE1!"))
    print(validate_password_strength("nouppercase1!"))
    print(validate_password_strength("NoDigits!x"))
    print(validate_password_strength("NoSpecial1x"))
    print(validate_password_strength("Short1!x"))