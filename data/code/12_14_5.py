import re

def validate_phone_number(phone: str) -> bool:
    pattern = r'^\+?1?[-.\s]?\(?[0-9]{3}\)?[-.\s]?[0-9]{3}[-.\s]?[0-9]{4}$'
    return bool(re.match(pattern, phone))

if __name__ == '__main__':
    phone_numbers = [
        "123-456-7890",
        "+1 (123) 456-7890",
        "123.456.7890",
        "123 456 7890",
        "(123) 456-7890",
        "1234567890",
        "+11234567890",
        "123-45-67890",
        "abc-def-ghij",
        "+44 123 456 7890",
    ]
    
    for number in phone_numbers:
        result = validate_phone_number(number)
        print(result)