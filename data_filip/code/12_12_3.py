import re

class PhoneNumberValidator:
    E164_PATTERN = re.compile(r'^\+[1-9]\d{6,14}$')

    @staticmethod
    def is_valid(number):
        if not isinstance(number, str):
            return False
        return bool(PhoneNumberValidator.E164_PATTERN.match(number))

    @staticmethod
    def validate_list(numbers):
        results = {}
        for number in numbers:
            results[number] = PhoneNumberValidator.is_valid(number)
        return results

if __name__ == '__main__':
    samples = [
        "+14155552671",
        "+442071838750",
        "+1234567890123456",
        "123456",
        "+12345",
        "+1234567890",
        "1234567890",
        "+0123456789"
    ]
    
    validator = PhoneNumberValidator()
    validation_results = PhoneNumberValidator.validate_list(samples)
    
    for number, is_valid in validation_results.items():
        print(f"{number}: {is_valid}")