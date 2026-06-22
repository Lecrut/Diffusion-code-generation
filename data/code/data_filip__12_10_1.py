import re

PHONE_PATTERN = re.compile(
    r"^\("
    r"\d{3}"
    r"\)"
    r"\s?"
    r"\d{3}"
    r"[-]?"
    r"\s?"
    r"\d{4}$"
)

def validate_phone(phone_number):
    if phone_number is None:
        return False
    if not isinstance(phone_number, str):
        return False
    if len(phone_number) < 10:
        return False
    stripped = phone_number.replace("-", "").replace("(", "").replace(")", "").replace(" ", "")
    if not stripped.isdigit():
        return False
    if len(stripped) != 10:
        return False
    if not PHONE_PATTERN.match(phone_number):
        return False
    return True

if __name__ == '__main__':
    test_numbers = [
        "1234567890",
        "(123) 456-7890",
        "123-456-7890",
        "123 456 7890",
        "(123)456-7890",
        "123456789",
        "123-456-789",
        "123-456-78901",
        "abcdef",
        "(123) 456-789",
        "",
        None,
        1234567890
    ]

    for num in test_numbers:
        result = validate_phone(num)
        print(result)