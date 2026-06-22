def is_valid_phone_number(phone_number):
    if not phone_number.startswith('+'):
        return False
    rest = phone_number[1:]
    if not rest:
        return False
    if not rest[0].isdigit():
        return False
    country_code_end = 1
    while country_code_end < len(rest) and country_code_end < 4:
        if rest[country_code_end].isdigit():
            country_code_end += 1
        else:
            break
    if country_code_end < 2 or country_code_end > 4:
        return False
    country_code = rest[:country_code_end]
    if not country_code.isdigit():
        return False
    if len(country_code) < 1 or len(country_code) > 3:
        return False
    number_part = rest[country_code_end:]
    if len(number_part) < 7 or len(number_part) > 10:
        return False
    if not number_part.isdigit():
        return False
    return True

if __name__ == '__main__':
    test_cases = [
        "+1234567890",
        "+1234567",
        "+4412345678901",
        "+123456",
        "1234567890",
        "+123456789012",
        "+99123456789",
        "+12345678"
    ]
    for case in test_cases:
        print(is_valid_phone_number(case))