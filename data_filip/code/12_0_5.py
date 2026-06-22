import re

def validate_e164(phone_number: str) -> bool:
    pattern = r'^\+\d{1,15}$'
    return bool(re.match(pattern, phone_number))

if __name__ == '__main__':
    test_number = "+12125551212"
    result = validate_e164(test_number)
    print(result)