import re

def validate_us_phone(phone: str) -> bool:
    pattern = r'^(\+1\s?)?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4}$'
    if not re.match(pattern, phone):
        return False
    digits = re.sub(r'\D', '', phone)
    if len(digits) == 11 and digits[0] == '1':
        digits = digits[1:]
    if len(digits) != 10:
        return False
    return True

if __name__ == '__main__':
    samples = ["(123) 456-7890", "123-456-7890", "1234567890", "123 456 7890", "1-123-456-7890", "1234"]
    for s in samples:
        print(validate_us_phone(s))