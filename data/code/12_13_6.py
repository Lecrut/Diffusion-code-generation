import re

PATTERN = re.compile(r'^\+?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$')

def format_phone(number):
    return re.sub(r'[^\d+]', '', number).strip()

def validate_phones(ph_list):
    valid = []
    for item in ph_list:
        clean = format_phone(item)
        if PATTERN.match(clean):
            valid.append(clean)
    return valid

if __name__ == '__main__':
    phones = [
        "+1 (555) 123-4567",
        "555-123-4567",
        "123.456.7890",
        "(555) 456 7890",
        "5551234567",
        "123-abc-4567",
        "Invalid Number",
        "+1 555 123 4567",
        "555-123-456",
    ]
    print(validate_phones(phones))