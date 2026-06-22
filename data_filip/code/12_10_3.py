import re

def validate_phone(phone: str) -> bool:
    pattern = re.compile(r'^(\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$')
    return bool(pattern.match(phone))

if __name__ == '__main__':
    print(validate_phone("(123) 456-7890"))
    print(validate_phone("123-456-7890"))
    print(validate_phone("1234567890"))
    print(validate_phone("1-123-456-7890"))
    print(validate_phone("123.456.7890"))
    print(validate_phone("123 456 7890"))
    print(validate_phone("11234567890"))
    print(validate_phone("123456789"))
    print(validate_phone("123-45-67890"))
    print(validate_phone("+1 (123) 456-7890"))
    print(validate_phone("abc-def-ghij"))
    print(validate_phone(""))