import re

def validate_phone_numbers(phone_numbers):
    normalized = re.compile(r'\+?[1-9]\d{1,2}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}')
    return [num for num in phone_numbers if normalized.fullmatch(num)]

if __name__ == '__main__':
    sample_numbers = [
        "+1-555-123-4567",
        "123-456-7890",
        "(555) 123-4567",
        "invalid-phone",
        "+44 20 7946 0958",
        "555.123.4567",
        "123456789012",
        "abc-def-ghij"
    ]
    valid_numbers = validate_phone_numbers(sample_numbers)
    print(valid_numbers)