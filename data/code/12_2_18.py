def validate_phone_number(phone_number):
    allowed_chars = set('0123456789 -()')
    for char in phone_number:
        if char not in allowed_chars:
            return False
    return True

if __name__ == '__main__':
    test_cases = [
        "123-456-7890",
        "(123) 456-7890",
        "123 456 7890",
        "123-456-7890x",
        "",
        "123+456",
        "(123) 456-7890 ext. 101"
    ]
    for case in test_cases:
        result = validate_phone_number(case)
        print(f"{case}: {result}")