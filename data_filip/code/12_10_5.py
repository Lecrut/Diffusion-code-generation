import re

pattern = re.compile(
    r'^(\+?1[-.\s]?)?'
    r'(\(?\d{3}\)?[-.\s]?)'
    r'\d{3}'
    r'[-.\s]?'
    r'\d{4}$'
)

def validate_phone(phone: str) -> bool:
    return bool(pattern.match(phone))

if __name__ == '__main__':
    print(validate_phone('1234567890'))
    print(validate_phone('123-456-7890'))
    print(validate_phone('(123) 456-7890'))
    print(validate_phone('1-123-456-7890'))
    print(validate_phone('123.456.7890'))
    print(validate_phone('123456789'))
    print(validate_phone('123-456-789'))
    print(validate_phone(''))