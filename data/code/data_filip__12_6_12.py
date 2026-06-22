def validate_phone_number(phone_number):
    if len(phone_number) < 7 or len(phone_number) > 15:
        return False
    for char in phone_number:
        if char.isalpha():
            return False
    return True

if __name__ == '__main__':
    test_cases = ["1234567", "123456789012345", "123456", "1234567890123456", "abc1234567", "123-456-7890", "123 456 7890"]
    for number in test_cases:
        result = validate_phone_number(number)
        print(result)