import re

def is_valid_phone_number(phone_str):
    if not isinstance(phone_str, str):
        return False
    pattern = r'^[\d\s\-\(\)]+$'
    return bool(re.fullmatch(pattern, phone_str))

if __name__ == '__main__':
    samples = [
        "123-456-7890",
        "(123) 456-7890",
        "123 456 7890",
        "1234567890",
        "123-45-6789",
        "123 456 7890 ext 1234",
        "",
        "123-456-78901",
        "abc-def-ghij",
        "+1 (123) 456-7890"
    ]
    for sample in samples:
        result = is_valid_phone_number(sample)
        print(result)