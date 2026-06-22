def validate_password(password):
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    if not (has_upper and has_lower and has_digit and has_special):
        return False
    for i in range(len(password) - 3):
        if password[i] == password[i+1] == password[i+2] == password[i+3]:
            return False
    return True

if __name__ == '__main__':
    test_passwords = [
        "Abc123!@#",
        "Aaaa123!@",
        "Short1!",
        "Valid1Pass!",
        "noLower123!@",
        "NOUPPER123!@",
        "NoSpecial123"
    ]
    for pwd in test_passwords:
        result = validate_password(pwd)
        print(f"{pwd}: {result}")