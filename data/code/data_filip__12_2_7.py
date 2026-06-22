def is_valid_phone_format(phone_number):
    allowed_chars = set("0123456789-() ")
    for char in phone_number:
        if char not in allowed_chars:
            return False
    return True

if __name__ == '__main__':
    test_cases = [
        "123-456-7890",
        "(123) 456-7890",
        "123 456 7890",
        "123-456-7890 ext. 123",
        "123@456",
        "",
        " 123 ",
        "123-abc-7890"
    ]
    
    for case in test_cases:
        result = is_valid_phone_format(case)
        print(f"Input: '{case}' -> Valid: {result}")