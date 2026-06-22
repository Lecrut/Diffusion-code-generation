def check_password_strength(password):
    has_upper = 0
    has_lower = 0
    has_digit = 0
    has_special = 0

    for char in password:
        code = ord(char)
        if 65 <= code <= 90:
            has_upper = 1
        elif 97 <= code <= 122:
            has_lower = 1
        elif 48 <= code <= 57:
            has_digit = 1
        else:
            has_special = 1

    strength_score = (has_upper << 3) | (has_lower << 2) | (has_digit << 1) | has_special
    return strength_score

if __name__ == '__main__':
    sample_passwords = [
        "Password1!",
        "hello",
        "12345",
        "ABCDE",
        "!@#$%",
        "Test1",
        "test1!",
        "T3st!ng",
    ]

    for pwd in sample_passwords:
        result = check_password_strength(pwd)
        print(f"{pwd}: {result}")