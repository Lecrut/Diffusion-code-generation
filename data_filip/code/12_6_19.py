def validate_phone_number(phone_number):
    if not isinstance(phone_number, str):
        return False
    if len(phone_number) < 7 or len(phone_number) > 15:
        return False
    if any(c.isalpha() for c in phone_number):
        return False
    return True

if __name__ == '__main__':
    print(validate_phone_number("1234567"))
    print(validate_phone_number("123456"))
    print(validate_phone_number("1234567890123456"))
    print(validate_phone_number("123abc456"))
    print(validate_phone_number("123-456-7890"))
    print(validate_phone_number(""))
    print(validate_phone_number("a" * 10))