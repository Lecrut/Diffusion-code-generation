import re
from typing import List

PHONE_PATTERN = re.compile(r'^\+?[1-9]\d{0,2}[-.\s]?\d{3}[-.\s]?\d{3}[-.\s]?\d{4}$')

def validate_phone_numbers(phone_numbers: List[str]) -> List[bool]:
    results = []
    for number in phone_numbers:
        is_valid = bool(PHONE_PATTERN.match(number))
        results.append(is_valid)
    return results

if __name__ == '__main__':
    hardcoded_numbers = [
        "123-456-7890",
        "+1-555-123-4567",
        "555.123.4567",
        "invalid-number",
        "12345",
        "(555) 123-4567"
    ]
    validation_results = validate_phone_numbers(hardcoded_numbers)
    for index, status in enumerate(validation_results):
        print(f"{hardcoded_numbers[index]}: {status}")