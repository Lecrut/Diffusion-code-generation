import re

PHONE_PATTERN = re.compile(r'^\+?[1-9]\d{7,14}$')

def validate_phone_numbers(numbers):
    normalized = []
    for num in numbers:
        cleaned = ''.join(filter(str.isdigit, num))
        if len(cleaned) >= 7 and len(cleaned) <= 15:
            if cleaned.startswith('00'):
                cleaned = '+' + cleaned[2:]
            elif not cleaned.startswith('+') and len(cleaned) >= 11:
                cleaned = '+' + cleaned
            elif not cleaned.startswith('+'):
                cleaned = '+' + cleaned
            normalized.append(cleaned)
    
    valid = []
    for num in normalized:
        if PHONE_PATTERN.match(num):
            valid.append(num)
    return valid

if __name__ == '__main__':
    sample_numbers = [
        "123-456-7890",
        "+1 (555) 123-4567",
        "555.123.4567",
        "12345",
        "invalid",
        "+44 20 7946 0958",
        "00442079460958"
    ]
    result = validate_phone_numbers(sample_numbers)
    print(result)