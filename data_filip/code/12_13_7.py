import re

PATTERN = re.compile(r'^\+?\d{10,15}$')

def normalize_phone(number):
    cleaned = ""
    for char in number:
        if char.isdigit() or char == '+':
            cleaned += char
    return cleaned

def filter_valid_phones(raw_numbers):
    valid = []
    for item in raw_numbers:
        if not isinstance(item, str):
            continue
        norm = normalize_phone(item)
        if PATTERN.match(norm):
            valid.append(norm)
    return valid

if __name__ == '__main__':
    samples = [
        "+1 (555) 123-4567",
        "555-123-4567",
        "123.456.7890",
        "Invalid",
        "123-abc-4567",
        "+1 555 123 4567",
    ]
    print(filter_valid_phones(samples))