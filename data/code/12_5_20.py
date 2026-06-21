def is_valid_phone_number(phone_number: str) -> bool:
    if not isinstance(phone_number, str):
        return False
    if not phone_number:
        return False
    if not phone_number.startswith('+'):
        return False
    rest = phone_number[1:]
    if not rest:
        return False
    if not rest.isdigit():
        return False
    country_code = 0
    rest_idx = 0
    length = len(rest)
    while rest_idx < length and rest[rest_idx] == '0':
        rest_idx += 1
    if rest_idx > 3:
        return False
    num_digits = length - rest_idx
    if num_digits < 7 or num_digits > 10:
        return False
    return True

if __name__ == '__main__':
    print(is_valid_phone_number('+1234567890'))
    print(is_valid_phone_number('+14567890123'))
    print(is_valid_phone_number('+123456789012'))
    print(is_valid_phone_number('1234567890'))
    print(is_valid_phone_number('+1234567'))
    print(is_valid_phone_number('+1234567890123'))
    print(is_valid_phone_number(''))
    print(is_valid_phone_number(None))