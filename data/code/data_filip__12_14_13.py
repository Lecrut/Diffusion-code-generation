import re

def validate_phone_number(phone: str) -> bool:
    pattern = r"^\+?[1-9]\d{1,14}$"
    return bool(re.match(pattern, phone))

def main() -> None:
    phone_numbers = [
        "+1234567890",
        "1234567890",
        "+0123456789",
        "123-456-7890",
        "+442079460123",
        "",
        "+1234567890123456",
        "abc123",
        "+8613800138000"
    ]

    for number in phone_numbers:
        result = validate_phone_number(number)
        print(result)

if __name__ == '__main__':
    main()