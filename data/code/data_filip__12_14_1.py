import re
from typing import List, Tuple, bool

def validate_phone_numbers(phone_list: List[str]) -> List[Tuple[str, bool]]:
    pattern = re.compile(r'^\+?1?\s?\d{3}[\s-]?\d{3}[\s-]?\d{4}$')
    results = []
    for number in phone_list:
        is_valid = bool(pattern.match(number))
        results.append((number, is_valid))
    return results

if __name__ == '__main__':
    sample_numbers = [
        "+1 202 555 0148",
        "555-0199",
        "12345",
        "+44 20 7946 0958",
        "(202) 555-0100",
        "202.555.0100",
        "invalid number",
        "1-800-555-0199"
    ]
    validation_results = validate_phone_numbers(sample_numbers)
    for original, status in validation_results:
        print(f"{original}: {status}")