def validate_phone_number(phone_number):
    if not phone_number:
        return False
    if not phone_number.startswith('+'):
        return False
    remaining = phone_number[1:]
    if not remaining.isdigit():
        return False
    if not (1 <= len(remaining) <= 13):
        return False
    country_code_length = len(remaining)
    if country_code_length < 1 or country_code_length > 3:
        return False
    national_number = remaining[country_code_length:]
    if not (7 <= len(national_number) <= 10):
        return False
    return True

if __name__ == '__main__':
    print(validate_phone_number('+1234567890'))
    print(validate_phone_number('+12345678'))
    print(validate_phone_number('+1234567'))
    print(validate_phone_number('+123456789012'))
    print(validate_phone_number('+1234567890123'))
    print(validate_phone_number('+12'))
    print(validate_phone_number('1234567890'))
    print(validate_phone_number('+abc1234567'))
    print(validate_phone_number('+1234567890a'))
    print(validate_phone_number(''))