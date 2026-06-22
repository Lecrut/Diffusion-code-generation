import re
import unicodedata

COMPILED_PATTERN = re.compile(r'^\+?[1-9]\d{0,3}[\s\-]?\(?\d{1,4}\)?[\s\-]?\d{3}[\s\-]?\d{3,4}$')

def normalize_phone_chars(phone_string):
    normalized = unicodedata.normalize('NFKD', phone_string)
    return ''.join(c for c in normalized if c.isascii() and (c.isdigit() or c in '+ -()'))

def filter_valid_phone_numbers(numbers):
    valid_numbers = []
    for number in numbers:
        normalized = normalize_phone_chars(number)
        if COMPILED_PATTERN.match(normalized):
            valid_numbers.append(normalized)
    return valid_numbers

if __name__ == '__main__':
    sample_numbers = [
        "123-456-7890",
        "+1 (800) 555-2671",
        "555.123.4567",
        "invalid_phone!",
        "1234567890",
        "+44 20 7946 0958",
        "abc-def-ghij",
        "   987-654-3210   "
    ]
    print(filter_valid_phone_numbers(sample_numbers))