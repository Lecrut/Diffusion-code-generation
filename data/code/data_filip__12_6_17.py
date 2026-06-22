def validate_phone_number(phone_number: str) -> bool:
    length = len(phone_number)
    if length < 7 or length > 15:
        return False
    for char in phone_number:
        if char.isalpha():
            return False
    return True

if __name__ == '__main__':
    phone1 = "1234567"
    phone2 = "1234567890"
    phone3 = "12345"
    phone4 = "1234567890123456"
    phone5 = "1234567a"
    phone6 = "8005551234"
    
    print(validate_phone_number(phone1))
    print(validate_phone_number(phone2))
    print(validate_phone_number(phone3))
    print(validate_phone_number(phone4))
    print(validate_phone_number(phone5))
    print(validate_phone_number(phone6))