import re

def validate_phone_numbers(numbers):
    normalized = []
    pattern = re.compile(r'^\+?[1-9]\d{1,14}$')
    for number in numbers:
        cleaned = re.sub(r'[\s\-\(\)\.]', '', number)
        if pattern.match(cleaned):
            normalized.append(cleaned)
    return normalized

if __name__ == '__main__':
    sample_numbers = [
        "+1-202-555-0199",
        "(202) 555.0100",
        "202-555-0101",
        "+44 20 7946 0958",
        "invalid",
        "123",
        "+1 800 555 1234",
        "abc-def-ghij"
    ]
    result = validate_phone_numbers(sample_numbers)
    print(result)