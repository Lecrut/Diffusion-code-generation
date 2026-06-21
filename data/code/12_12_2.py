import re

class PhoneNumberValidator:
    _E164_PATTERN = re.compile(r'^\+[1-9]\d{1,14}$')

    @staticmethod
    def is_valid(number: str) -> dict:
        if not isinstance(number, str):
            return {"number": number, "valid": False, "message": "Input must be a string"}
        
        if not number:
            return {"number": number, "valid": False, "message": "Input cannot be empty"}
        
        match = PhoneNumberValidator._E164_PATTERN.match(number)
        
        if match:
            return {"number": number, "valid": True, "message": "Valid E.164 phone number"}
        
        return {"number": number, "valid": False, "message": "Invalid E.164 phone number"}

if __name__ == '__main__':
    samples = [
        "+12025551234",
        "+44 7911 123456",
        "+91 9876543210",
        "12025551234",
        "+001234567890",
        "+12345678901234567890",
        "",
        "+12025551234"
    ]

    results = []
    for sample in samples:
        result = PhoneNumberValidator.is_valid(sample)
        results.append(result)

    for r in results:
        print(r)