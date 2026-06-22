def check_password(password):
    has_lower = 0
    has_upper = 0
    has_digit = 0
    has_special = 0
    
    for char in password:
        code = ord(char)
        has_lower = has_lower | ((code - 97) >> 31) & ((-((code - 97) >> 63)) & 1)
        has_lower = has_lower | ((code - 122) >> 31) & ((-((code - 122) >> 63)) & 1)
        
        temp_lower = ((code - 97) >> 31) & ((-((code - 97) >> 63)) & 1)
        if temp_lower == 0 and (code >= 97) and (code <= 122):
            has_lower = 1
        
        if (code >= 65) and (code <= 90):
            has_upper = 1
        if (code >= 48) and (code <= 57):
            has_digit = 1
        if (code == 33) or (code == 64) or (code == 35) or (code == 36) or (code == 37) or (code == 94) or (code == 38) or (code == 42):
            has_special = 1
            
    return has_lower and has_upper and has_digit and has_special

if __name__ == '__main__':
    test_passwords = ["SecurePass1!", "weakpass", "NOLOWER1", "NoDigits!"]
    for pwd in test_passwords:
        print(check_password(pwd))