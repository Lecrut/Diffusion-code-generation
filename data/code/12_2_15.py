def is_valid_phone_format(phone_number):
    allowed_chars = set("0123456789 -()")
    for char in phone_number:
        if char not in allowed_chars:
            return False
    return True

if __name__ == '__main__':
    test_cases = [
        "123-456-7890",
        "(123) 456-7890",
        "123 456 7890",
        "123-456-7890 ext. 1234",
        "abc-123-4567",
        "12345",
        "(123) 456-7890 x123"
    ]
    for test in test_cases:
        result = is_valid_phone_format(test)
        print(result)