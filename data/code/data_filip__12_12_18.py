import re

class PhoneNumberValidator:
    @staticmethod
    def is_valid(phone_number):
        cleaned = re.sub(r'[^\d+]', '', phone_number)
        pattern = r'^\+?[1-9]\d{6,14}$'
        match = re.fullmatch(pattern, cleaned)
        original_clean = cleaned if cleaned else ""
        return {
            "original": phone_number,
            "cleaned": original_clean,
            "is_valid": bool(match),
            "length": len(original_clean) if original_clean else 0
        }

if __name__ == '__main__':
    samples = ["+1234567890", "+44 20 7946 0958", "123-456-7890", "555-0199", "+1 (555) 123-4567", "+8613912345678", "invalid", "+123456789012345678901234567890"]
    validator_instance = PhoneNumberValidator()
    for sample in samples:
        result = validator_instance.is_valid(sample)
        print(result)