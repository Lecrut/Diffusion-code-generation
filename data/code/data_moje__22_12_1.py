import timeit

def check_password_strength(password):
    if not isinstance(password, str):
        return False
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
        
        if 97 <= code <= 122:
            has_lower = True
            lower_mask |= (1 << (code - 97))
        elif 65 <= code <= 90:
            has_upper = True
            upper_mask |= (1 << (code - 65))
        elif 48 <= code <= 57:
            has_digit = True
            digit_mask |= (1 << (code - 48))
        else:
            has_special = True
            special_mask |= 1
    
    if not (has_lower and has_upper and has_digit and has_special):
        return False
    
    bits_lower = bin(lower_mask).count('1')
    bits_upper = bin(upper_mask).count('1')
    bits_digit = bin(digit_mask).count('1')
    
    entropy_bits = 0
    if bits_lower > 0:
        entropy_bits += bits_lower * 4.7
    if bits_upper > 0:
        entropy_bits += bits_upper * 4.7
    if bits_digit > 0:
        entropy_bits += bits_digit * 3.3
    if has_special:
        entropy_bits += 6.0
    
    penalty = 0
    i = 0
    length = len(password)
    while i < length - 2:
        if password[i] == password[i+1] == password[i+2]:
            penalty += 2
            i += 3
        elif password[i] == password[i+2] and password[i] != password[i+1]:
            penalty += 1
            i += 2
        else:
            i += 1
    
    if len(password) < 12:
        penalty += 2
    
    if has_lower and has_upper and has_digit and has_special:
        penalty -= 1
    
    if entropy_bits - penalty < 50:
        return False
    
    return True

if __name__ == '__main__':
    test_passwords = [
        "Str0ng!Pass",
        "weak",
        "alllowercase",
        "12345678",
        "My$ecur3P@ssw0rd!"
    ]
    
    results = []
    for pwd in test_passwords:
        result = check_password_strength(pwd)
        results.append(result)
    
    print(results)
    strong_count = sum(1 for r in results if r)
    print(strong_count)