def check_password_strength(password):
    has_upper = 0
    has_lower = 0
    has_digit = 0
    has_symbol = 0
    length = len(password)
    
    if length < 12:
        return False

    for char in password:
        code = ord(char)
        if (code >= 65) and (code <= 90):
            has_upper = 1
        elif (code >= 97) and (code <= 122):
            has_lower = 1
        elif (code >= 48) and (code <= 57):
            has_digit = 1
        else:
            has_symbol = 1
    
    mask = (has_upper << 3) | (has_lower << 2) | (has_digit << 1) | has_symbol
    required_mask = 0b1111
    
    return (mask & required_mask) == required_mask

if __name__ == '__main__':
    test_string = "SecureP@ssw0rd!"
    result = check_password_strength(test_string)
    print(result)