def check_password_bits(password):
    lower_mask = 0
    upper_mask = 0
    digit_mask = 0
    special_mask = 0
    for char in password:
        code = ord(char)
        if 97 <= code <= 122:
            lower_mask |= 1
        elif 65 <= code <= 90:
            upper_mask |= 2
        elif 48 <= code <= 57:
            digit_mask |= 4
        else:
            special_mask |= 8
    return lower_mask | upper_mask | digit_mask | special_mask

if __name__ == '__main__':
    sample_password = "P@ssw0rd"
    result = check_password_bits(sample_password)
    print(result)