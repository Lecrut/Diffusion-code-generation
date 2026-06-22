import re

PHONE_NUMBERS = [
    "123-456-7890",
    "123.456.7890",
    "1234567890",
    "(123) 456-7890",
    "123 456 7890",
    "12345",
    "12345678901",
    "abc-def-ghij",
    "+1-123-456-7890",
    "000-000-0000",
]

def filter_standard_phone_numbers(numbers):
    pattern = r'^(?:\+?1[-.\s]?)?(?:\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{4}$'
    return [num for num in numbers if re.match(pattern, num)]

if __name__ == '__main__':
    result = filter_standard_phone_numbers(PHONE_NUMBERS)
    print(result)