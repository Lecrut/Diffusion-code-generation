def is_valid_phone_number(phone_number):
    digits = ''.join(c for c in phone_number if c.isdigit())
    return len(digits) == 11

if __name__ == '__main__':
    sample_numbers = [
        "+86 138 0000 1234",
        "13800001234",
        "138-0000-1234",
        "1380000123",
        "abc13800001234def"
    ]
    for number in sample_numbers:
        result = is_valid_phone_number(number)
        print(result)