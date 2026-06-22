def check_password(password):
    has_lower = 0
    has_upper = 0
    has_digit = 0
    has_special = 0
    special_chars = "!@#$%^&*()-_=+[]{}|;:,.<>?/"
    
    for char in password:
        code = ord(char)
        has_lower |= (code >= 97) & (code <= 122) << 0
        has_upper |= (code >= 65) & (code <= 90) << 1
        has_digit |= (code >= 48) & (code <= 57) << 2
        if char in special_chars:
            has_special |= 1 << 3
    
    has_lower = 1 if (has_lower & 1) else 0
    has_upper = 1 if (has_upper >> 1 & 1) else 0
    has_digit = 1 if (has_digit >> 2 & 1) else 0
    has_special = 1 if (has_special >> 3 & 1) else 0
    
    return has_lower and has_upper and has_digit and has_special

if __name__ == '__main__':
    sample_password = "SecureP@ss123"
    result = check_password(sample_password)
    print(result)
    sample_password_2 = "weak"
    result_2 = check_password(sample_password_2)
    print(result_2)