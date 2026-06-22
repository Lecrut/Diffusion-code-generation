import re
from typing import List, Tuple

PHONE_PATTERN = r'^\+?\d{1,3}?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'

def validate_phone_numbers(numbers: List[str]) -> List[Tuple[str, bool]]:
    results = []
    for number in numbers:
        match = re.fullmatch(PHONE_PATTERN, number)
        is_valid = match is not None
        results.append((number, is_valid))
    return results

if __name__ == '__main__':
    sample_phones = [
        '+1 (555) 123-4567',
        '555-123-4567',
        '123.456.7890',
        'invalid-phone',
        '+44 20 7946 0958'
    ]
    
    validated_results = validate_phone_numbers(sample_phones)
    
    for phone, is_valid in validated_results:
        print(is_valid)