import re

def validate_e164_phone(phone: str) -> bool:
    pattern = r'^\+[1-9]\d{1,14}$'
    return bool(re.match(pattern, phone))

if __name__ == '__main__':
    result1 = validate_e164_phone("+14155552671")
    result2 = validate_e164_phone("14155552671")
    result3 = validate_e164_phone("+919876543210")
    
    print(result1)
    print(result2)
    print(result3)