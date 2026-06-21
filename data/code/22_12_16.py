def check_password_strength(password):
    length = len(password)
    if length < 12:
        return False
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    for char in password:
        code = ord(char)
        if 65 <= code <= 90:
            has_upper = True
        elif 97 <= code <= 122:
            has_lower = True
        elif 48 <= code <= 57:
            has_digit = True
        else:
            has_special = True
        if has_upper and has_lower and has_digit and has_special:
            return True
    return False

if __name__ == '__main__':
    test_password = "Str0ng!Pass"
    print(check_password_strength(test_password))