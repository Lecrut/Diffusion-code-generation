def is_valid_phone_number(phone):
    if not phone:
        return False
    if not phone.startswith('+'):
        return False
    
    rest = phone[1:]
    if not rest:
        return False
    
    if not rest[0].isdigit():
        return False
    
    plus_digits_count = 0
    temp = rest
    while temp and temp[0].isdigit():
        plus_digits_count += 1
        temp = temp[1:]
    
    if plus_digits_count < 1 or plus_digits_count > 3:
        return False
    
    if not temp:
        return False
    
    main_digits_count = 0
    while temp and temp[0].isdigit():
        main_digits_count += 1
        temp = temp[1:]
    
    if main_digits_count < 7 or main_digits_count > 10:
        return False
    
    if temp:
        return False
    
    return True

if __name__ == '__main__':
    test_cases = ["+12345678901", "+447911123456", "+1234567", "+123456789", "+44123456789012", "+1234567890", "+1234567890a", "+123456", "+12345678"]
    for phone in test_cases:
        print(is_valid_phone_number(phone))