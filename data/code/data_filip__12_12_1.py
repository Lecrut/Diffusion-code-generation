import re

class PhoneNumberValidator:
    E164_PATTERN = re.compile(r'^\+[1-9]\d{1,14}$')

    @staticmethod
    def is_valid(phone_number):
        if not isinstance(phone_number, str):
            return {"valid": False, "reason": "Input must be a string"}
        if not phone_number:
            return {"valid": False, "reason": "Input cannot be empty"}
        if PhoneNumberValidator.E164_PATTERN.match(phone_number):
            return {"valid": True, "reason": "Valid E.164 format", "number": phone_number}
        return {"valid": False, "reason": "Invalid E.164 format", "number": phone_number}

if __name__ == '__main__':
    sample_numbers = ["+14155552671", "+442071838750", "1234567890", "+1-555-0199", "+999", "", "+12"]
    validator = PhoneNumberValidator()
    results = []
    for number in sample_numbers:
        result = validator.is_valid(number)
        results.append(result)
    print(results)