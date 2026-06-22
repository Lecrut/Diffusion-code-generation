import re

def validate_phone_number(phone_number: str) -> bool:
    if not phone_number:
        return False
    pattern = r'^[0-9 ()-]+$'
    return bool(re.match(pattern, phone_number))

if __name__ == '__main__':
    test_cases = [
        "123-456-7890",
        "(123) 456-7890",
        "123 456 7890",
        "123-456-7890 ext 123",
        "abc-def-ghij",
        "",
        "1234567890",
        "(999) 111-2222",
        "555- 1234",
    ]

    for number in test_cases:
        result = validate_phone_number(number)
        print(result)