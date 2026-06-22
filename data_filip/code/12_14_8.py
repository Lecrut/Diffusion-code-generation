import re
from typing import List, Tuple

def validate_phone_numbers(phone_list: List[str], pattern: str) -> List[Tuple[str, bool]]:
    compiled_pattern = re.compile(pattern)
    results: List[Tuple[str, bool]] = []
    for number in phone_list:
        is_valid = bool(compiled_pattern.fullmatch(number))
        results.append((number, is_valid))
    return results

if __name__ == '__main__':
    hardcoded_numbers = ["+1234567890", "123-456-7890", "(123) 456-7890", "123.456.7890", "abc-def-ghij"]
    regex_pattern = r'^\+?\d{1,3}[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'
    validation_results = validate_phone_numbers(hardcoded_numbers, regex_pattern)
    for entry, status in validation_results:
        print(f"{entry}: {status}")