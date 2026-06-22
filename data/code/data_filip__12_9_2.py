def validate_international_dialing_code(code: str) -> bool:
    if not isinstance(code, str):
        raise TypeError("Input must be a string")
    if not code:
        return False
    if not code.startswith('+'):
        return False
    digits_part = code[1:]
    if not digits_part.isdigit():
        return False
    if len(digits_part) < 1 or len(digits_part) > 15:
        return False
    return True

if __name__ == '__main__':
    print(validate_international_dialing_code('+1'))
    print(validate_international_dialing_code('+447911123456'))
    print(validate_international_dialing_code('123'))
    print(validate_international_dialing_code('+1abc'))
    print(validate_international_dialing_code('+'))
    print(validate_international_dialing_code(''))
    print(validate_international_dialing_code('+123456789012345'))
    print(validate_international_dialing_code('+1234567890123456'))