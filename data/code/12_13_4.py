import re

def validate_phone_numbers():
    pattern = re.compile(r'^\+?\d{1,3}?\d{3,14}$')
    phones = ["(123) 456-7890", "123-456-7890", "+1 123 456 7890", "123.456.7890", "invalid", "+44 1234 567890"]
    normalized = []
    for phone in phones:
        clean = re.sub(r'[^0-9+]', '', phone)
        if pattern.match(clean):
            normalized.append(phone)
    return normalized

if __name__ == '__main__':
    result = validate_phone_numbers()
    print(result)