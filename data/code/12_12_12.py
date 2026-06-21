import re

class PhoneNumberValidator:
    E164_PATTERN = re.compile(r'^\+[1-9]\d{1,14}$')

    @staticmethod
    def is_valid(number_string):
        if not isinstance(number_string, str):
            return {'valid': False, 'error': 'Input must be a string'}
        if not PhoneNumberValidator.E164_PATTERN.match(number_string):
            return {'valid': False, 'error': 'Does not match E.164 format'}
        return {'valid': True, 'error': None}

if __name__ == '__main__':
    sample_numbers = [
        "+1234567890",
        "+447911123456",
        "1234567890",
        "+1-234-567-890",
        "+0123456789",
        "+123",
        "",
        "+123456789012345678"
    ]
    
    validator = PhoneNumberValidator()
    results = {}
    for number in sample_numbers:
        results[number] = PhoneNumberValidator.is_valid(number)
    
    for number, result in results.items():
        print(f"Number: {number}, Result: {result}")