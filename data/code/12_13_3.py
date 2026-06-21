import re
import unicodedata

COMPILED_PATTERN = re.compile(r"^\+?[1-9]\d{6,14}$")

def normalize_number(number: str) -> str:
    normalized = unicodedata.normalize("NFKC", number)
    return "".join(c for c in normalized if c.isdigit() or c == "+")

def filter_valid_phone_numbers(phone_list: list) -> list:
    valid_numbers = []
    for item in phone_list:
        normalized = normalize_number(item)
        if COMPILED_PATTERN.match(normalized):
            valid_numbers.append(normalized)
    return valid_numbers

if __name__ == "__main__":
    sample_numbers = [
        "+1-555-123-4567",
        "(555) 987-6543",
        "1234567890123",
        "invalid",
        "0000",
        "+44 20 7946 0958",
        "  +1 800 555 0199  ",
        "999"
    ]
    result = filter_valid_phone_numbers(sample_numbers)
    print(result)