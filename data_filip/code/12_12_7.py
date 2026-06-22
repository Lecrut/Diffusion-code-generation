import re

class PhoneNumberValidator:
    _e164_pattern = re.compile(r'^\+[1-9]\d{1,14}$')

    @staticmethod
    def is_valid(number):
        match = PhoneNumberValidator._e164_pattern.match(number)
        return bool(match)

if __name__ == '__main__':
    samples = [
        "+14155552671",
        "+442071234567",
        "+8613800138000",
        "+12345678901234567",
        "1234567890",
        "+",
        "+0123456789",
        "+1234567890",
        "+1-415-555-2671",
        "+79123456789"
    ]
    results = {sample: PhoneNumberValidator.is_valid(sample) for sample in samples}
    print(results)