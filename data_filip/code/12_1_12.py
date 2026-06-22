import re

def process_phone_number(phone):
    digits = re.sub(r'\D', '', phone)
    if len(digits) == 11:
        return digits
    return None

if __name__ == '__main__':
    sample_cases = ["+1 (555) 123-4567", "12345678901", "abc123def45678901"]
    for case in sample_cases:
        result = process_phone_number(case)
        print(result)