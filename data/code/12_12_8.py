import re

class PhoneValidator:
    @staticmethod
    def is_valid(phone_number):
        if not isinstance(phone_number, str):
            return {"valid": False, "error": "Input must be a string"}
        pattern = r'^\+[1-9]\d{1,14}$'
        if re.match(pattern, phone_number):
            digits_only = re.sub(r'[^\d]', '', phone_number)
            return {"valid": True, "number": phone_number, "digits": digits_only, "length": len(digits_only)}
        return {"valid": False, "error": "Does not match E.164 format"}

if __name__ == '__main__':
    samples = [
        "+12025551234",
        "+442079460018",
        "+33123456789",
        "1234567890",
        "+1-202-555-1234",
        "+1202555123",
        "0012025551234",
        "+12025551234567890123456789"
    ]
    validator = PhoneValidator()
    results = []
    for sample in samples:
        results.append(validator.is_valid(sample))
    for res in results:
        print(res)