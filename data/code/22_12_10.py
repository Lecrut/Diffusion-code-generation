def check_password_strength(password):
    length_ok = len(password) >= 12
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    special_chars = set("!@#$%^&*()_+-=[]{}|;:',.<>?/~`")
    
    for char in password:
        code = ord(char)
        if 65 <= code <= 90:
            has_upper = True
        elif 97 <= code <= 122:
            has_lower = True
        elif 48 <= code <= 57:
            has_digit = True
        elif char in special_chars:
            has_special = True
            
    strength_bits = 0
    if length_ok:
        strength_bits |= 1
    if has_upper:
        strength_bits |= 2
    if has_lower:
        strength_bits |= 4
    if has_digit:
        strength_bits |= 8
    if has_special:
        strength_bits |= 16
        
    is_strong = (strength_bits == 31)
    return strength_bits, is_strong

if __name__ == '__main__':
    test_password = "SecureP@ssw0rd!"
    bits, strong = check_password_strength(test_password)
    print(bits)
    print(strong)