def validate_phone_number(phone_number: str) -> bool:
    length = len(phone_number)
    if length < 7 or length > 15:
        return False
    for char in phone_number:
        if char.isalpha():
            return False
    return True

if __name__ == '__main__':
    print(validate_phone_number("1234567"))
    print(validate_phone_number("123456"))
    print(validate_phone_number("1234567890123456"))
    print(validate_phone_number("123abc789"))
    print(validate_phone_number("123-456-7890"))