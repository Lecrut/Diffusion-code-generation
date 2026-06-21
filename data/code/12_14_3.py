import re

PHONE_NUMBERS = [
    "+1-212-555-1234",
    "(555) 123-4567",
    "555.123.4567",
    "123-45-6789",
    "+44 20 7946 0958",
    "abc-def-ghij",
    "",
    "+1 212 555 1234",
    "1234567890",
]

def validate_phone_number(number: str) -> bool:
    if not number:
        return False
    pattern = r"^\+?\d{1,3}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}$"
    return bool(re.fullmatch(pattern, number))

if __name__ == '__main__':
    results = [validate_phone_number(num) for num in PHONE_NUMBERS]
    for num, is_valid in zip(PHONE_NUMBERS, results):
        print(f"{num!r}: {is_valid}")