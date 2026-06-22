import re
from typing import List

def validate_phone_numbers(phone_list: List[str]) -> List[bool]:
    pattern = re.compile(r'^\+?1?\s?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$')
    results = []
    for number in phone_list:
        is_valid = bool(pattern.match(number))
        results.append(is_valid)
    return results

if __name__ == '__main__':
    sample_numbers = [
        "123-456-7890",
        "+1 (555) 123-4567",
        "555.012.3456",
        "123456789",
        "123-45-6789",
        "+1-800-555-0199",
        "(800) 555-0199"
    ]
    validation_status = validate_phone_numbers(sample_numbers)
    for status in validation_status:
        print(status)