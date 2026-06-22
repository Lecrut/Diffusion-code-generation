import re

class E164Validator:
    _PATTERN = re.compile(r'^\+[1-9][0-9]{1,14}$')

    @staticmethod
    def is_valid(phone: str) -> dict:
        if not isinstance(phone, str):
            return {"input": phone, "valid": False, "reason": "non-string input"}
        if not phone:
            return {"input": phone, "valid": False, "reason": "empty string"}
        if E164Validator._PATTERN.match(phone):
            return {"input": phone, "valid": True, "reason": "compliant"}
        return {"input": phone, "valid": False, "reason": "non-compliant"}

if __name__ == '__main__':
    test_cases = ["+14155552671", "+442071838750", "1234567890", "+1-555-0199", "", "+999", "+12", 123]
    validator = E164Validator()
    for case in test_cases:
        print(validator.is_valid(case))