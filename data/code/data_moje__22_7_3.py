def check_password(password):
    has_lower = 0
    has_upper = 0
    has_digit = 0
    has_symbol = 0
    
    for char in password:
        code = ord(char)
        
        if 97 <= code <= 122:
            has_lower |= 1
        elif 65 <= code <= 90:
            has_upper |= 2
        elif 48 <= code <= 57:
            has_digit |= 4
        elif code in (33, 35, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 58, 59, 60, 61, 62, 63, 64, 91, 92, 93, 94, 95, 96, 123, 124, 125, 126):
            has_symbol |= 8
    
    return (has_lower == 1) and (has_upper == 2) and (has_digit == 4) and (has_symbol == 8)

if __name__ == '__main__':
    sample_password = "Test1234!"
    result = check_password(sample_password)
    print(result)