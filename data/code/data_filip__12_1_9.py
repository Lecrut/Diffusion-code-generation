import re

def normalize_phone_number(phone: str) -> bool:
    digits_only = re.sub(r'\D', '', phone)
    return len(digits_only) == 11

if __name__ == '__main__':
    sample_phones = ['+1 (234) 567-8901', '123-456-78901', '12345', '01234567890']
    for phone in sample_phones:
        result = normalize_phone_number(phone)
        print(result)