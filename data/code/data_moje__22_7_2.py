def check_password(password: str) -> dict:
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in password:
        code = ord(char)
        
        if 65 <= code <= 90:
            has_upper = True
        elif 97 <= code <= 122:
            has_lower = True
        elif 48 <= code <= 57:
            has_digit = True
        else:
            has_special = True

    return {
        'has_upper': has_upper,
        'has_lower': has_lower,
        'has_digit': has_digit,
        'has_special': has_special
    }

if __name__ == '__main__':
    sample_password = "Koolaid#2023"
    result = check_password(sample_password)
    print(result)