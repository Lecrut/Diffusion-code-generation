import re
from typing import List, Tuple

def validate_phone_numbers(phone_list: List[str]) -> List[Tuple[str, bool]]:
    pattern = re.compile(r'^\+?1?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$')
    results = []
    for number in phone_list:
        is_valid = bool(pattern.match(number))
        results.append((number, is_valid))
    return results

if __name__ == '__main__':
    sample_numbers = [
        "123-456-7890",
        "+1 (555) 123-4567",
        "5551234567",
        "invalid-number",
        "(123) 456-789",
        "1-800-555-0199"
    ]
    validation_results = validate_phone_numbers(sample_numbers)
    for number, status in validation_results:
        print(f"{number}: {status}")