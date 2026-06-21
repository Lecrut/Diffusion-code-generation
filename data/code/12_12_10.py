import re

class PhoneValidator:
    _pattern = re.compile(r'^\+[1-9]\d{1,14}$')

    @staticmethod
    def is_valid(phone_number):
        match = PhoneValidator._pattern.match(phone_number)
        return {
            'value': phone_number,
            'is_valid': bool(match),
            'length': len(phone_number)
        }

    @classmethod
    def validate_batch(cls, numbers):
        results = []
        for number in numbers:
            results.append(cls.is_valid(number))
        return results

if __name__ == '__main__':
    samples = [
        '+12025550198',
        '+442079460958',
        '+8613912345678',
        '12025550198',
        '+123',
        '+01234567890',
        '+1234567890123456',
        '+12 025550198',
        '',
        '+441234567890'
    ]
    validator = PhoneValidator()
    results = validator.validate_batch(samples)
    for result in results:
        print(result)