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
        elif not (65 <= code <= 90 or 97 <= code <= 122 or 48 <= code <= 57):
            has_special = 1

    return has_upper | has_lower << 1 | has_digit << 2 | has_special << 3

if __name__ == '__main__':
    print(check_password_strength("Hello"))
    print(check_password_strength("Hello1"))
    print(check_password_strength("Hello1!"))
    print(check_password_strength("HELLO1!"))