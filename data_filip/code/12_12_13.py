import re

class E164Checker:
    STANDARD_PATTERN = re.compile(r'^\+[1-9]\d{1,14}$')

    @staticmethod
    def is_valid(number):
        if not isinstance(number, str):
            return {"input": number, "is_valid": False, "error": "input_not_string"}
        if not number:
            return {"input": number, "is_valid": False, "error": "input_empty"}
        if E164Checker.STANDARD_PATTERN.match(number):
            return {"input": number, "is_valid": True, "error": None}
        return {"input": number, "is_valid": False, "error": "format_mismatch"}

if __name__ == '__main__':
    test_entries = [
        "+14155552671",
        "+442071838750",
        "+919876543210",
        "1234567890",
        "+1-555-0199",
        "",
        "+12",
        "+99999999999999999",
        "abc",
        "+0123456789"
    ]
    validator = E164Checker()
    output = []
    for entry in test_entries:
        res = validator.is_valid(entry)
        output.append(res)
    print(output)