import re
import unicodedata

COMPILED_PATTERN = re.compile(r'^\+?1?[-.\s]?\(?[0-9]{3}\)?[-.\s]?[0-9]{3}[-.\s]?[0-9]{4}$')

def normalize_and_validate(numbers):
    normalized_numbers = []
    for num in numbers:
        try:
            normalized = unicodedata.normalize('NFKC', num).strip()
            if COMPILED_PATTERN.match(normalized):
                normalized_numbers.append(normalized)
        except Exception:
            continue
    return normalized_numbers

if __name__ == '__main__':
    sample_data = [
        "+1 (555) 123-4567",
        "555-123-4567",
        "1 555 123 4567",
        "invalid-phone",
        "555.123.4567",
        "123",
        "+44 20 7946 0958",
        "5551234567"
    ]
    result = normalize_and_validate(sample_data)
    print(result)