import re

def validate_phone_numbers(phone_numbers):
    pattern = re.compile(r'^\+?[1-9]\d{1,14}$')
    return [bool(pattern.match(number)) for number in phone_numbers]

if __name__ == '__main__':
    sample_phone_numbers = [
        "+1234567890",
        "1234567890",
        "+49 123 45678",
        "123-456-7890",
        "+442071234567",
        "00442071234567",
        "invalid",
        "+1",
        "+123456789012345"
    ]
    validation_results = validate_phone_numbers(sample_phone_numbers)
    for number, is_valid in zip(sample_phone_numbers, validation_results):
        print(f"{number}: {is_valid}")