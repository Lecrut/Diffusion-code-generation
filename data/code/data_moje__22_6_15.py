def validate_password(password):
    if len(password) < 8:
        return False
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = set("!@#$%^&*()_+-=[]{}|;:',.<>?/")
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True
    
    if not (has_upper and has_lower and has_digit):
        return False
    
    max_repeats = 1
    current_repeats = 1
    
    for i in range(1, len(password)):
        if password[i] == password[i - 1]:
            current_repeats += 1
            if current_repeats > max_repeats:
                max_repeats = current_repeats
        else:
            current_repeats = 1
        
        if max_repeats > 3:
            return False
    
    return True

if __name__ == '__main__':
    result = validate_password("Abc123!")
    print(result)
    
    result2 = validate_password("Aaa123!")
    print(result2)
    
    result3 = validate_password("Abc1")
    print(result3)
    
    result4 = validate_password("aaaa123A!")
    print(result4)