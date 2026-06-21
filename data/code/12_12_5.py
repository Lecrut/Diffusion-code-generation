import re

class PhoneNumberValidator:
    E164_PATTERN = re.compile(r"^\+?[1-9]\d{6,14}$")

    @staticmethod
    def is_valid(phone_number):
        if not isinstance(phone_number, str):
            return False
        return bool(PhoneNumberValidator.E164_PATTERN.match(phone_number))

if __name__ == "__main__":
    samples = ["+12125551234", "+442071838750", "123", "+1-555-1234", "+80012345678", "+1234567", "abc", "", "+1234567890123456", "99"]
    results = {}
    for s in samples:
        results[s] = PhoneNumberValidator.is_valid(s)
    print(results)