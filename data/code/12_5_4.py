def is_valid_phone_number(phone_number):
    if not phone_number or phone_number[0] != '+':
        return False
    digits = phone_number[1:]
    if not digits:
        return False
    for char in digits:
        if not char.isdigit():
            return False
    total_length = len(digits)
    if total_length < 8:
        return False
    if total_length > 13:
        return False
    if total_length <= 10:
        return True
    return False

if __name__ == '__main__':
    test_cases = [
        "+1234567890",
        "+11234567",
        "+441234567890",
        "+123456789012",
        "+12345678901",
        "+1234567",
        "+12345678901234",
        "1234567890",
        "+123456789",
        "+1234567890123",
        "+123456789012345",
        "+1234567890123",
    ]
    for case in test_cases:
        print(is_valid_phone_number(case))