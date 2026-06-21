import re
from typing import List

def validate_phone_numbers(phone_numbers: List[str]) -> List[bool]:
    pattern = re.compile(r'^\+?[1-9]\d{1,14}$')
    results = []
    for number in phone_numbers:
        is_valid = bool(pattern.match(number))
        results.append(is_valid)
    return results

if __name__ == '__main__':
    sample_numbers = ["+1234567890", "123-456-7890", "555.012.3456", "+442071838750", "000", "1"]
    validation_results = validate_phone_numbers(sample_numbers)
    for number, is_valid in zip(sample_numbers, validation_results):
        print(is_valid)