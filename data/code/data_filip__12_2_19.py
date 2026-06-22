import re

def is_valid_phone_number(phone: str) -> bool:
    return bool(re.fullmatch(r'[0-9 ()\-]+', phone))

if __name__ == '__main__':
    samples = [
        "123-456-7890",
        "(123) 456-7890",
        "123 456 7890",
        "123-45-6789",
        "123-456-789",
        "1234567890",
        "abc-123-4567",
        "123 456 7890x",
        "",
        "1234",
        "123-456-78901",
    ]
    for sample in samples:
        print(is_valid_phone_number(sample))