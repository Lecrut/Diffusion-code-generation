def is_valid_phone_number(phone_number):
    if not isinstance(phone_number, str) or not phone_number:
        return False
    if phone_number[0] != '+':
        return False
    
    remaining = phone_number[1:]
    if not remaining:
        return False
    
    digits_start = ""
    i = 0
    while i < len(remaining) and remaining[i].isdigit():
        digits_start += remaining[i]
        i += 1
    
    if len(digits_start) < 1 or len(digits_start) > 3:
        return False
    
    if i >= len(remaining):
        return False
    
    if remaining[i] == '+':
        return False
    
    rest_digits = ""
    while i < len(remaining) and remaining[i].isdigit():
        rest_digits += remaining[i]
        i += 1
    
    if i != len(remaining):
        return False
    
    if len(rest_digits) < 7 or len(rest_digits) > 10:
        return False
    
    return True

if __name__ == '__main__':
    test_numbers = [
        "+12345678901",
        "+1234567890",
        "+123456789",
        "+12345678",
        "+1234567",
        "+123456789012",
        "+1234567890123",
        "1234567890",
        "+1234567",
        "+12345678901234",
        "+12 345 678 901",
        "+1234567890a",
        "++1234567890",
        "+12345678901"
    ]
    for number in test_numbers:
        print(is_valid_phone_number(number))