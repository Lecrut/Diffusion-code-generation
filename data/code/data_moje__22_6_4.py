def validate_password_strength(password):
    if len(password) < 8:
        return False
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = set("!@#$%^&*()_+-=[]{}|;:,.<>?/")
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True
    if not (has_upper and has_lower and has_digit and has_special):
        return False
    count = 1
    for i in range(1, len(password)):
        if password[i] == password[i - 1]:
            count += 1
            if count > 3:
                return False
        else:
            count = 1
    return True

if __name__ == '__main__':
    print(validate_password_strength("Password1!"))
    print(validate_password_strength("Pass1234!"))
    print(validate_password_strength("Passssword1!"))
    print(validate_password_strength("Short1!"))
    print(validate_password_strength("NoSpecialChar123"))