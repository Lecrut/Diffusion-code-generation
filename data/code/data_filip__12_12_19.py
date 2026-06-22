import re

class PhoneValidator:
    _pattern = re.compile(r'^\+[1-9]\d{1,14}$')

    @staticmethod
    def is_valid(phone_number: str) -> dict:
        if not isinstance(phone_number, str):
            return {'number': phone_number, 'is_valid': False, 'reason': 'not a string'}
        
        match = PhoneValidator._pattern.match(phone_number)
        if match:
            digits = phone_number[1:]
            return {
                'number': phone_number,
                'is_valid': True,
                'country_code': digits[:2] if len(digits) > 11 else digits[:1],
                'subscriber_number': digits[2:] if len(digits) > 2 else digits,
                'reason': None
            }
        
        return {
            'number': phone_number,
            'is_valid': False,
            'reason': 'invalid format'
        }

if __name__ == '__main__':
    validator = PhoneValidator()
    samples = [
        "+14155552671",
        "+442071234567",
        "+919876543210",
        "+112345",
        "+000000000000",
        "14155552671",
        "+1invalid123"
    ]
    
    results = []
    for sample in samples:
        result = validator.is_valid(sample)
        results.append(result)
    
    print(results)