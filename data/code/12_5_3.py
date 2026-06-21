def is_valid_phone_number(phone: str) -> bool:
    if not isinstance(phone, str):
        return False
    if len(phone) == 0:
        return False
    if phone[0] != '+':
        return False
    rest = phone[1:]
    if len(rest) == 0:
        return False
    if not rest.isdigit():
        return False
    
    country_code = ""
    i = 0
    n = len(rest)
    while i < n:
        char = rest[i]
        if not char.isdigit():
            break
        if len(country_code) >= 3:
            break
        country_code += char
        i += 1
    
    if len(country_code) < 1 or len(country_code) > 3:
        return False
    
    if i < n and rest[i] == '+':
        return False
    
    remaining = rest[i:]
    if len(remaining) < 7 or len(remaining) > 10:
        return False
    
    if not remaining.isdigit():
        return False
    
    return True

if __name__ == '__main__':
    print(is_valid_phone_number("+12345678901"))
    print(is_valid_phone_number("+14567890"))
    print(is_valid_phone_number("+12345678"))
    print(is_valid_phone_number("1234567890"))
    print(is_valid_phone_number("+456789"))
    print(is_valid_phone_number("+123456789012"))
    print(is_valid_phone_number("+"))
    print(is_valid_phone_number("++1234567890"))