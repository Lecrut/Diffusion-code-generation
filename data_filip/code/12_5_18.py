def validate_phone_number(phone_number: str) -> bool:
    if not phone_number:
        return False
    
    if not phone_number.startswith('+'):
        return False
    
    rest = phone_number[1:]
    
    if not rest.isdigit():
        return False
    
    length = len(rest)
    
    if length < 8 or length > 13:
        return False
    
    first_part = rest[:3]
    second_part = rest[3:]
    
    if len(first_part) < 1 or len(first_part) > 3:
        return False
    
    if len(second_part) < 7 or len(second_part) > 10:
        return False
    
    if len(first_part) + len(second_part) != length:
        return False
    
    return True

if __name__ == '__main__':
    result1 = validate_phone_number('+1234567890')
    print(result1)
    
    result2 = validate_phone_number('+1456789')
    print(result2)
    
    result3 = validate_phone_number('1234567890')
    print(result3)
    
    result4 = validate_phone_number('+12345678901234')
    print(result4)