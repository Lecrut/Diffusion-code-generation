import re

def validate_phone_number(phone: str) -> bool:
    pattern = r'^\+?1?\d{9,15}$'
    return bool(re.match(pattern, phone))

def main() -> None:
    phone_numbers = [
        "+1234567890",
        "1234567890",
        "123-456-7890",
        "+44 20 7946 0958",
        "00442079460958",
        "abc123456",
        "",
        "+1-800-555-1234",
        "18005551234",
        "+44207946095"
    ]
    for number in phone_numbers:
        print(validate_phone_number(number))

if __name__ == '__main__':
    main()