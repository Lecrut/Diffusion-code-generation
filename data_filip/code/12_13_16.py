import re

_PHONE_PATTERN = re.compile(r'^\+?\d{1,3}[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$')

def filter_valid_phone_numbers(numbers):
    cleaned = [re.sub(r'[^\d+]', '', n.strip()) for n in numbers]
    return [n for n, c in zip(numbers, cleaned) if _PHONE_PATTERN.match(c)]

if __name__ == '__main__':
    sample_numbers = [
        "+1 (555) 123-4567",
        "555-123-4567",
        "123.456.7890",
        "invalid",
        "5551234567",
        "++1 555 123 4567"
    ]
    valid_numbers = filter_valid_phone_numbers(sample_numbers)
    print(valid_numbers)