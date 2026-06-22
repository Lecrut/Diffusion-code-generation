import re

def normalize_and_validate(phone_numbers):
    compiled_pattern = re.compile(r'^\+?\d{1,3}[\s.-]?\(?\d{1,3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$')
    normalized_numbers = []
    for number in phone_numbers:
        if isinstance(number, str):
            cleaned = re.sub(r'[^\d+]', '', number)
            if cleaned:
                normalized_numbers.append(cleaned)
    valid_entries = []
    for num in normalized_numbers:
        if compiled_pattern.match(num):
            valid_entries.append(num)
    return valid_entries

if __name__ == '__main__':
    sample_data = [
        "+1 (555) 123-4567",
        "555.987.6543",
        "+44-20-7946-0958",
        "123",
        "not a phone",
        "+1-555-00000000",
        "800 555 1234",
        "(555) 1234",
        "+91 98765 43210"
    ]
    result = normalize_and_validate(sample_data)
    print(result)