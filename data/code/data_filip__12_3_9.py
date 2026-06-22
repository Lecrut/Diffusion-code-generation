import re

def validate_us_phone_number(phone_number):
    pattern = re.compile(r'^\s*\(\d{3}\)\s*\d{3}[-]?\d{4}\s*$|^\s*\d{3}[-]\d{3}[-]\d{4}\s*$')
    if pattern.match(phone_number):
        cleaned = phone_number.replace(' ', '').replace('(', '').replace(')', '').replace('-', '')
        if len(cleaned) == 10 and cleaned.isdigit():
            return True
    return False

if __name__ == '__main__':
    test_cases = ["(123) 456-7890", "123-456-7890", "123 456 7890", "1234567890", "abc-def-ghij", "(123) 45-6789"]
    for case in test_cases:
        result = validate_us_phone_number(case)
        print(f"Phone: {case} -> Valid: {result}")