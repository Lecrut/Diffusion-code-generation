import re

PHONE_PATTERN = re.compile(r"^\+?[1-9]\d{1,14}$")

def validate_phone_numbers(numbers: list[str]) -> list[bool]:
    results = []
    for number in numbers:
        if PHONE_PATTERN.match(number):
            results.append(True)
        else:
            results.append(False)
    return results

if __name__ == '__main__':
    phone_numbers = [
        "+1234567890",
        "1234567890",
        "invalid-number",
        "+1-234-567-890",
        "123"
    ]
    validation_statuses = validate_phone_numbers(phone_numbers)
    for number, status in zip(phone_numbers, validation_statuses):
        print(status)