import re

def validate_phone_numbers(phone_numbers):
    pattern = re.compile(r'^\+?[1-9]\d{1,14}$')
    
    def normalize(phone):
        return re.sub(r'[\s\-\(\)]', '', phone)
    
    return [phone for phone in phone_numbers if pattern.match(normalize(phone))]

if __name__ == '__main__':
    sample_phones = [
        "+1 (555) 123-4567",
        "555.123.4567",
        "+44 20 7946 0958",
        "invalid-phone",
        "+81 3-1234-5678",
        "123",
        "+1 800 123 4567"
    ]
    print(validate_phone_numbers(sample_phones))