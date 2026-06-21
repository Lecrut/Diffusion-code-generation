def validate_password_strength(password):
    if len(password) < 8:
        return False
    
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    special_characters = set("!@#$%^&*()_+-=[]{}|;:,.<>?/~`")
    
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
    test_cases = [
        "Password1!",
        "weak",
        "NoDigitsHere!",
        "nolowercase1!",
        "NOUPPER1!",
        "NoSpecial1",
        "Short1!",
        "Perfect1Pass!"
    ]
    
    for password in test_cases:
        result = validate_password_strength(password)
        print(result)