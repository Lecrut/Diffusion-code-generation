def check_password_strength(password):
    length = len(password)
    if length < 12:
        return False

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    upper_mask = 0
    lower_mask = 0
    digit_mask = 0
    special_mask = 0

    for char in password:
        code = ord(char)

        if 65 <= code <= 90:
            upper_mask |= 1
            has_upper = True
        elif 97 <= code <= 122:
            lower_mask |= 1
            has_lower = True
        elif 48 <= code <= 57:
            digit_mask |= 1
            has_digit = True
        else:
            special_mask |= 1
            has_special = True

    requirements_met = has_upper & has_lower & has_digit & has_special

    return requirements_met

if __name__ == '__main__':
    test_password = "Str0ng!Pass#99"
    result = check_password_strength(test_password)
    print(result)