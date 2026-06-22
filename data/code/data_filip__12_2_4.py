def validate_phone_number(phone_number):
    allowed_characters = set('0123456789 -()')
    return all(char in allowed_characters for char in phone_number)

if __name__ == '__main__':
    print(validate_phone_number("123-456-7890"))
    print(validate_phone_number("(123) 456-7890"))
    print(validate_phone_number("123.456.7890"))
    print(validate_phone_number("abc-def-ghij"))
    print(validate_phone_number("123 456 7890"))
    print(validate_phone_number(""))
    print(validate_phone_number("123-456-7890!"))
    print(validate_phone_number("(123)456-7890"))