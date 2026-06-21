import re

def normalize_phone(number):
    return re.sub(r'[^\d]', '', number)

def filter_valid_phones(phone_list):
    pattern = re.compile(r'^\d{10,15}$')
    valid_entries = []
    for phone in phone_list:
        normalized = normalize_phone(phone)
        if pattern.match(normalized):
            valid_entries.append(normalized)
    return valid_entries

if __name__ == '__main__':
    sample_numbers = [
        "(555) 123-4567",
        "1-800-555-0199",
        "555.123.4567",
        "12345",
        "invalid-phone",
        "+1 555 123 4567",
        "9876543210"
    ]
    print(filter_valid_phones(sample_numbers))