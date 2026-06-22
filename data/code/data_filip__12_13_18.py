import re

PHONE_NUMBERS = [
    "(123) 456-7890",
    "123-456-7890",
    "123.456.7890",
    "123 456 7890",
    "1234567890",
    "+1-123-456-7890",
    "123-abc-7890",
    "invalid",
    "123456",
    "+1 123 456 7890",
]

_PATTERN = re.compile(r"^\+?1?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$")

def validate_phone_numbers(numbers):
    return [num for num in numbers if _PATTERN.match(num)]

if __name__ == '__main__':
    valid_numbers = validate_phone_numbers(PHONE_NUMBERS)
    print(valid_numbers)