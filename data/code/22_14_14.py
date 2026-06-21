COMMON_WEAK_PASSWORDS = {
    "password", "123456", "12345678", "qwerty", "abc123", "monkey", "master",
    "dragon", "111111", "baseball", "iloveyou", "trustno1", "sunshine",
    "ashley", "football", "shadow", "123123", "654321", "superman",
    "qazwsx", "michael", "password1", "password123", "letmein", "welcome",
    "hotspot", "666666", "qwertyuiop", "123321", "mustang", "1234567890"
}

def is_sequential(password, length=3):
    if len(password) < length:
        return False
    for i in range(len(password) - length + 1):
        sequential = True
        for j in range(1, length):
            if ord(password[i + j]) != ord(password[i + j - 1]) + 1:
                sequential = False
                break
        if sequential:
            return True
    return False

def validate_password_strength(password):
    if not password:
        return False
    if len(password) < 8:
        return False
    if password.lower() in COMMON_WEAK_PASSWORDS:
        return False
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special = True
    if not (has_upper and has_lower and has_digit and has_special):
        return False
    if is_sequential(password):
        return False
    return True

if __name__ == '__main__':
    test_passwords = [
        "Password1!",
        "weakpass",
        "12345678",
        "StrongP@ss1",
        "abcABC123!",
        "Abc123!@#",
        "HelloWorld",
        "Pass1234",
        "MyS3cur3P@ss!",
        "abcdefg1!",
        "A1b2c3d4!",
        "password123",
        "Qwerty1!",
        "Tr0ub4dor&3",
        "123abcABC!",
        "Simple1!"
    ]
    for pwd in test_passwords:
        result = validate_password_strength(pwd)
        print(f"{pwd}: {result}")