import re

class PhoneValidator:
    E164_PATTERN = re.compile(r"^\+?[1-9]\d{1,14}$")

    @staticmethod
    def is_valid(number):
        if not isinstance(number, str):
            return {"valid": False, "reason": "Input must be a string"}
        if not PhoneValidator.E164_PATTERN.match(number):
            return {"valid": False, "reason": "Does not match E.164 format"}
        return {"valid": True, "reason": "Valid E.164 format"}

if __name__ == "__main__":
    sample_numbers = ["+14155552671", "+442071838750", "123", "+123456789012345678", "+1-800-555-0199", "+0000000000"]
    results = []
    for num in sample_numbers:
        results.append(PhoneValidator.is_valid(num))
    print(results)