def validate_phone_number(phone_number: str) -> bool:
    digits = ''.join(c for c in phone_number if c.isdigit())
    return len(digits) == 11

if __name__ == '__main__':
    sample1 = "+1 (555) 123-4567"
    sample2 = "15551234567"
    sample3 = "555-1234"
    print(validate_phone_number(sample1))
    print(validate_phone_number(sample2))
    print(validate_phone_number(sample3))