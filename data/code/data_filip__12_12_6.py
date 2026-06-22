import re

class PhoneNumberValidator:
    _e164_pattern = re.compile(r'^\+[1-9]\d{1,14}$')
    
    @staticmethod
    def is_valid(phone_number):
        if not isinstance(phone_number, str):
            return {'input': str(phone_number), 'is_valid': False, 'reason': 'Invalid type'}
        if PhoneNumberValidator._e164_pattern.match(phone_number):
            return {'input': phone_number, 'is_valid': True, 'reason': 'Valid E.164 format'}
        else:
            return {'input': phone_number, 'is_valid': False, 'reason': 'Invalid E.164 format'}

if __name__ == '__main__':
    samples = ["+12025551234", "+442071234567", "1234567890", "+12345", "+01234567890", "", "+1", "+999999999999999"]
    validator = PhoneNumberValidator()
    results = []
    for sample in samples:
        result = validator.is_valid(sample)
        results.append(result)
    print(results)