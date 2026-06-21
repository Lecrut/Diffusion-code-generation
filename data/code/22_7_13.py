def check_password_strength(password):
    has_lower = 0
    has_upper = 0
    has_digit = 0
    has_special = 0
    
    mask_lower = 0x01
    mask_upper = 0x02
    mask_digit = 0x04
    mask_special = 0x08
    
    flags = 0
    
    for char in password:
        code = ord(char)
        
        if 97 <= code <= 122:
            flags |= mask_lower
        elif 65 <= code <= 90:
            flags |= mask_upper
        elif 48 <= code <= 57:
            flags |= mask_digit
        else:
            flags |= mask_special
            
    return flags

if __name__ == '__main__':
    sample_password = "Abc123!@#"
    result = check_password_strength(sample_password)
    print(result)