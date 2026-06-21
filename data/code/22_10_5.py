def validate_password_strength(password):
    if len(password) < 8:
        return False
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True
    return has_upper and has_lower and has_digit and has_special

if __name__ == '__main__':
    samples = [
        "short",
        "nouppercase1!",
        "NOLOWERCASE1!",
        "NoDigitsHere!",
        "NoSpecial1!",
        "ValidPass1!",
        "AnotherValid9#"
    ]
    for sample in samples:
        result = validate_password_strength(sample)
        print(result)