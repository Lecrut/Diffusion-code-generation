def check_password_strength(password):
    has_lower = 0
    has_upper = 0
    has_digit = 0
    has_special = 0
    for char in password:
        code = ord(char)
        lower_start = ord('a')
        lower_end = ord('z')
        upper_start = ord('A')
        upper_end = ord('Z')
        digit_start = ord('0')
        digit_end = ord('9')
        if lower_start <= code <= lower_end:
            has_lower |= 1
        elif upper_start <= code <= upper_end:
            has_upper |= 2
        elif digit_start <= code <= digit_end:
            has_digit |= 4
        else:
            has_special |= 8
    mask = has_lower | has_upper | has_digit | has_special
    return (has_lower != 0) and (has_upper != 0) and (has_digit != 0) and (has_special != 0)

if __name__ == '__main__':
    sample_password = "SecurePass1!"
    result = check_password_strength(sample_password)
    print(result)