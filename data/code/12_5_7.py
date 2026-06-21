def check_phone_number(phone_number):
    if not isinstance(phone_number, str):
        return False
    if not phone_number:
        return False
    if phone_number[0] != '+':
        return False
    rest = phone_number[1:]
    if not rest.isdigit():
        return False
    if len(rest) < 1 or len(rest) > 13:
        return False
    country_code_len = 0
    digit_index = 0
    while digit_index < len(rest) and country_code_len < 3:
        if not rest[digit_index].isdigit():
            return False
        country_code_len += 1
        digit_index += 1
    remaining_digits = len(rest) - country_code_len
    if country_code_len < 1:
        return False
    if remaining_digits < 7 or remaining_digits > 10:
        return False
    return True

if __name__ == '__main__':
    samples = [
        "+1234567890",
        "+12345678",
        "+1234567",
        "+12345678901234",
        "+123456789012345",
        "1234567890",
        "+abc1234567",
        "+12",
        "+12345678901",
        "+123456789012",
        "+1234567890123",
        "",
        "+",
        "+1",
        "+123456789"
    ]
    for sample in samples:
        print(check_phone_number(sample))