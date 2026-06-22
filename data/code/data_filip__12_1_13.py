def validate_phone_number(phone_number: str) -> bool:
    digits = ''.join(c for c in phone_number if c.isdigit())
    return len(digits) == 11

if __name__ == '__main__':
    sample1 = "123-456-7890"
    sample2 = "+1 (123) 456-7890"
    sample3 = "09876543210"
    sample4 = "12345"

    print(validate_phone_number(sample1))
    print(validate_phone_number(sample2))
    print(validate_phone_number(sample3))
    print(validate_phone_number(sample4))