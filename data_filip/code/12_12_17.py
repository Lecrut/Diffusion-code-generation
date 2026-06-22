import re

class PhoneValidator:

    @staticmethod
    def is_valid(phone_number):
        pattern = r'^\+[1-9]\d{1,14}$'
        if not isinstance(phone_number, str):
            return {"valid": False, "number": phone_number, "message": "Input is not a string"}
        match = re.match(pattern, phone_number)
        if match:
            return {"valid": True, "number": phone_number, "message": "E.164 compliant"}
        return {"valid": False, "number": phone_number, "message": "Invalid E.164 format"}

if __name__ == '__main__':
    validator = PhoneValidator()
    samples = [
        "+12125551212",
        "+447911123456",
        "+123",
        "12125551212",
        "+12125551212x1",
        ""
    ]
    results = [validator.is_valid(s) for s in samples]
    print(results)