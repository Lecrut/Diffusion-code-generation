def validate_password(password: str) -> dict:
    if len(password) < 8:
        return {'valid': False, 'errors': ['Password must be at least 8 characters long']}
    errors = []
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = set('!@#$%^&*()-_=+[]{}|;:,.<>?/`~')
    i = 0
    length = len(password)
    while i < length:
        char = password[i]
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True
        j = i
        while j < length and password[j] == char:
            j += 1
        if j - i > 3:
            errors.append(f"Password contains too many repeating characters ('{char}' repeated {j - i} times)")
            break
        i = j
    if not has_upper:
        errors.append('Password must contain at least one uppercase letter')
    if not has_lower:
        errors.append('Password must contain at least one lowercase letter')
    if not has_digit:
        errors.append('Password must contain at least one digit')
    if not has_special:
        errors.append('Password must contain at least one special character')
    return {'valid': len(errors) == 0, 'errors': errors}
if __name__ == '__main__':
    test_passwords = ['Short1!', 'noUppercase1!', 'nouppercase1!', 'nouppercase!', 'Short!Aa', 'Valid123!', 'aaabbbccc1!', 'aaaa123!']
    for pwd in test_passwords:
        result = validate_password(pwd)
        print(f"Password: '{pwd}' -> Valid: {result['valid']}, Errors: {result['errors']}")