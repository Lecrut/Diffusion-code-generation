import re

E164_REGEX = re.compile(r'^\+[1-9]\d{6,14}$')

def validate_e164(phone_number: str) -> bool:
    return bool(E164_REGEX.match(phone_number))

if __name__ == '__main__':
    result = validate_e164("+12025551234")
    print(result)
    
    result_invalid = validate_e164("12025551234")
    print(result_invalid)
    
    result_another_valid = validate_e164("+447911123456")
    print(result_another_valid)