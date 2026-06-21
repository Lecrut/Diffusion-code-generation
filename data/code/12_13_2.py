import re

PHONE_NUMBERS = [
    "+1 (555) 123-4567",
    "555-123-4567",
    "123.456.7890",
    "(555) 456 7890",
    "5551234567",
    "123-abc-4567",
    "Invalid Number",
    "+1 555 123 4567",
    "555-123-456",
]

_PATTERN = re.compile(r"^\+?1?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$")

def validate_phone_numbers(numbers):
    return [num for num in numbers if _PATTERN.match(num.replace(" ", "").replace("-", "").replace(".", "").replace("(", "").replace(")", "").replace("+", ""))]

if __name__ == '__main__':
    result = validate_phone_numbers(PHONE_NUMBERS)
    print(result)