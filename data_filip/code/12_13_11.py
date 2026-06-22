import re

def validate_phone_numbers(phone_numbers):
    pattern = re.compile(r'^\+?[1-9]\d{1,14}$')
    
    def normalize(number):
        return ''.join(c for c in number if c.isdigit() or c == '+')
    
    return [normalized for number in phone_numbers for normalized in [normalize(number)] if pattern.match(normalized)]

if __name__ == '__main__':
    sample_numbers = [
        "+1-234-567-8901",
        "234.567.8901",
        "+44 113 496 0986",
        "invalid number",
        "+1 (234) 567-8901",
        "12345678901",
        "+123456789012345",
        "abc-def-ghij",
        "+86-138-0013-8000"
    ]
    valid_numbers = validate_phone_numbers(sample_numbers)
    print(valid_numbers)