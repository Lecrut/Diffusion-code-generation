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

    strength_bits = has_upper << 3 | has_lower << 2 | has_digit << 1 | has_special
    return strength_bits

if __name__ == '__main__':
    sample_passwords = [
        "Hello",
        "hello123",
        "Hello123",
        "Hello123!",
        "123456",
        "ABCDEF",
        "!@#$%",
        "ComplexP@ssw0rd"
    ]
    for pwd in sample_passwords:
        result = check_password_strength(pwd)
        print(result)