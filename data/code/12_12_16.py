import re

class PhoneValidator:
    _e164_pattern = re.compile(r'^\+[1-9]\d{1,14}$')

    @staticmethod
    def is_valid(phone_number: str) -> dict:
        stripped = phone_number.strip()
        is_match = PhoneValidator._e164_pattern.match(stripped) is not None
        return {
            'input': phone_number,
            'valid': is_match,
            'normalized': stripped if is_match else None
        }

    @classmethod
    def validate_batch(cls, phone_numbers: list) -> list:
        return [cls.is_valid(number) for number in phone_numbers]

if __name__ == '__main__':
    sample_numbers = [
        '+14155552671',
        '+442071234567',
        '+861012345678',
        '1234567890',
        '+01234567890',
        '+1',
        '+1234567890123456',
        '  +14155552671  ',
        '+33123456789',
        '+491701234567'
    ]

    validator = PhoneValidator()
    results = validator.validate_batch(sample_numbers)
    print(results)