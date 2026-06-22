import re
from typing import List, Tuple

def validate_phone_numbers(phone_list: List[str]) -> List[Tuple[str, bool]]:
    pattern = re.compile(r'^\+?[1-9]\d{9,14}$')
    results = []
    for number in phone_list:
        is_valid = bool(pattern.match(number))
        results.append((number, is_valid))
    return results

if __name__ == '__main__':
    hardcoded_numbers = [
        "+14155552671",
        "14155552671",
        "555-0199",
        "123456789012345",
        "invalid_number",
        "+442071838750"
    ]
    validation_results = validate_phone_numbers(hardcoded_numbers)
    for number, status in validation_results:
        print(status)