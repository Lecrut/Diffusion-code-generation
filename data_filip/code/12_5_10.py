def validate_phone_number(phone_str: str) -> bool:
    if not phone_str:
        return False
    if phone_str[0] != '+':
        return False
    rest = phone_str[1:]
    if not rest:
        return False
    if not rest.isdigit():
        return False
    country_code_part = rest.split(' ')[0] if ' ' in rest else rest
    if ' ' in rest:
        remaining_digits = rest[len(country_code_part):].replace(' ', '')
    else:
        remaining_digits = ''
    
    if len(country_code_part) < 1 or len(country_code_part) > 3:
        return False
    
    if not remaining_digits:
        return False
    
    if len(remaining_digits) < 7 or len(remaining_digits) > 10:
        return False
        
    return True

if __name__ == '__main__':
    print(validate_phone_number("+11234567890"))
    print(validate_phone_number("+4471234567"))
    print(validate_phone_number("+123456789"))
    print(validate_phone_number("+1234567"))
    print(validate_phone_number("1234567890"))
    print(validate_phone_number("+12345678901"))