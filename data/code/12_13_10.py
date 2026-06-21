import re

PHONE_PATTERN = re.compile(r'^\+?[1-9]\d{1,14}$')

def validate_phone_numbers(numbers):
    normalized_numbers = []
    for number in numbers:
        cleaned = ''.join(filter(str.isdigit, number))
        if not cleaned.startswith('0') and len(cleaned) >= 7 and len(cleaned) <= 15:
            normalized_numbers.append(cleaned)
    
    valid_entries = []
    for num in normalized_numbers:
        if PHONE_PATTERN.match(num):
            valid_entries.append(num)
    return valid_entries

if __name__ == '__main__':
    sample_data = [
        "123-456-7890",
        "+1 (555) 123-4567",
        "invalid number",
        "555-0199",
        "+44 20 7946 0958",
        "000-000-0000",
        "12345678901234567890"
    ]
    print(validate_phone_numbers(sample_data))