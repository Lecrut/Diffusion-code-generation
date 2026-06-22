import re

class E164Checker:
    PATTERN = re.compile(r'^\+[1-9]\d{1,14}$')

    @staticmethod
    def is_valid(phone_number):
        if not isinstance(phone_number, str) or not phone_number:
            return {"valid": False, "number": phone_number}
        if E164Checker.PATTERN.match(phone_number):
            return {"valid": True, "number": phone_number}
        return {"valid": False, "number": phone_number}

if __name__ == '__main__':
    samples = ["+14155552671", "+442071838750", "1234567890", "+1-555-0199", "+999", "", "+12"]
    checker = E164Checker()
    for num in samples:
        print(checker.is_valid(num))