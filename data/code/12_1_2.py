def validate_phone_number(phone_number: str) -> str:
    digits = ''.join(c for c in phone_number if c.isdigit())
    if len(digits) == 11:
        return digits
    return ""

if __name__ == '__main__':
    sample_1 = "+1 (555) 123-4567"
    sample_2 = "12345678901"
    sample_3 = "987-654-3210"
    result_1 = validate_phone_number(sample_1)
    result_2 = validate_phone_number(sample_2)
    result_3 = validate_phone_number(sample_3)
    print(result_1)
    print(result_2)
    print(result_3)