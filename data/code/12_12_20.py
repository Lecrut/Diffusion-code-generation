import re

class PhoneValidator:
    E164_PATTERN = re.compile(r'^\+[1-9]\d{1,14}$')

    @staticmethod
    def is_valid(phone_number):
        if not isinstance(phone_number, str):
            return {"valid": False, "reason": "Input must be a string"}
        if len(phone_number) > 15:
            return {"valid": False, "reason": "Too many digits"}
        if PhoneValidator.E164_PATTERN.match(phone_number):
            return {"valid": True, "reason": "Compliant with E.164"}
        return {"valid": False, "reason": "Invalid format"}

if __name__ == "__main__":
    samples = [
        "+12025551234",
        "+447911123456",
        "1234567890",
        "+1234",
        "+19876543210",
        "+8612345678901",
        "+01234567890",
        "+1-202-555-0199",
        "abc+1234567890"
    ]
    validator = PhoneValidator()
    results = []
    for sample in samples:
        result = validator.is_valid(sample)
        results.append({"input": sample, "validation": result})
    print(results)