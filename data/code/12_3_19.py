import re

def is_valid_us_phone_number(phone: str) -> bool:
    pattern = r"^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$"
    return bool(re.fullmatch(pattern, phone))

if __name__ == '__main__':
    results = [
        is_valid_us_phone_number("(123) 456-7890"),
        is_valid_us_phone_number("123-456-7890"),
        is_valid_us_phone_number("123.456.7890"),
        is_valid_us_phone_number("1234567890"),
        is_valid_us_phone_number("123 456 7890"),
        is_valid_us_phone_number("123-456-789"),
        is_valid_us_phone_number("(123) 456-789"),
        is_valid_us_phone_number("123-456-7890x123"),
    ]
    print(results)