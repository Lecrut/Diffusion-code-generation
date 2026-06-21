def check_password_strength(password):
    has_upper = 0
    has_lower = 0
    has_digit = 0
    has_special = 0
    for char in password:
        code = ord(char)
        if 65 <= code <= 90:
            has_upper = 1
        if 97 <= code <= 122:
            has_lower = 1
        if 48 <= code <= 57:
            has_digit = 1
        if not (has_upper or has_lower or has_digit):
            has_special = 1
    return (has_upper << 3) | (has_lower << 2) | (has_digit << 1) | has_special

if __name__ == '__main__':
    print(check_password_strength("Password1!"))
    print(check_password_strength("hello"))
    print(check_password_strength("12345"))
    print(check_password_strength("ABCDEF"))
    print(check_password_strength("!@#$%"))