import re

def is_valid_us_phone(phone: str) -> bool:
    pattern = r'^(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'
    cleaned = re.sub(r'[^\d]', '', phone)
    if len(cleaned) == 10:
        if re.match(r'^\d{3}\d{3}\d{4}$', phone):
            return True
        if re.match(r'^\(\d{3}\) \d{3}-\d{4}$', phone):
            return True
        if re.match(r'^\d{3}-\d{3}-\d{4}$', phone):
            return True
    if len(cleaned) == 11 and cleaned[0] == '1':
        if re.match(r'^1\(\d{3}\) \d{3}-\d{4}$', phone):
            return True
        if re.match(r'^1 \(\d{3}\) \d{3}-\d{4}$', phone):
            return True
        if re.match(r'^1-\(\d{3}\) \d{3}-\d{4}$', phone):
            return True
        if re.match(r'^1\d{3}\d{3}\d{4}$', phone):
            return True
        if re.match(r'^1\d{3}-\d{3}-\d{4}$', phone):
            return True
        if re.match(r'^\(1\d{3}\) \d{3}-\d{4}$', phone):
            return True
    return False

if __name__ == '__main__':
    test_numbers = ["(123) 456-7890", "123-456-7890", "1234567890", "1-123-456-7890", "123-45-6789", "(123) 456-789"]
    for number in test_numbers:
        print(is_valid_us_phone(number))