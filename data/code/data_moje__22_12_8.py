import string

def check_password_strength(password):
    if len(password) < 8:
        return False
    
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    
    lower_mask = 0
    upper_mask = 0
    digit_mask = 0
    special_mask = 0
    
    for char in password:
        code = ord(char)
        
        if code >= 97 and code <= 122:
            has_lower = True
            lower_mask |= (1 << (code - 97))
        elif code >= 65 and code <= 90:
            has_upper = True
            upper_mask |= (1 << (code - 65))
        elif code >= 48 and code <= 57:
            has_digit = True
            digit_mask |= (1 << (code - 48))
        elif char in string.punctuation:
            has_special = True
            special_mask |= 1
            
    if not (has_lower and has_upper and has_digit and has_special):
        return False
        
    char_count = len(password)
    unique_chars = bin(lower_mask).count('1') + bin(upper_mask).count('1') + bin(digit_mask).count('1') + special_mask
    
    if unique_chars < 4:
        return False
        
    consecutive_count = 0
    max_consecutive = 0
    
    for i in range(1, len(password)):
        if password[i] == password[i-1]:
            consecutive_count += 1
            if consecutive_count > max_consecutive:
                max_consecutive = consecutive_count
        else:
            consecutive_count = 0
            
    if max_consecutive >= 3:
        return False
        
    if (len(password) % 2) == 0:
        if len(password) % 4 == 0:
            return False
            
    return True

if __name__ == '__main__':
    test_password = "Str0ng!P@ssw0rd"
    result = check_password_strength(test_password)
    print(result)
    test_password_2 = "weak"
    result_2 = check_password_strength(test_password_2)
    print(result_2)
    test_password_3 = "AllSame1!"
    result_3 = check_password_strength(test_password_3)
    print(result_3)