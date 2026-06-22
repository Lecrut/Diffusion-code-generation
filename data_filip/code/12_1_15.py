def validate_phone_number(phone_number: str) -> bool:
    stripped = ''.join(char for char in phone_number if char.isdigit())
    return len(stripped) == 11

if __name__ == '__main__':
    print(validate_phone_number("+1 (234) 567-8901"))
    print(validate_phone_number("12345678901"))
    print(validate_phone_number("123-456-7890"))
    print(validate_phone_number("hello12345678901world"))
    print(validate_phone_number("1234567890"))