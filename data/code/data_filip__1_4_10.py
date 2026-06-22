import re
import sys

class EmailValidator:
    @staticmethod
    def validate(email):
        if not isinstance(email, str):
            return False
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email) is not None

if __name__ == '__main__':
    validator = EmailValidator()
    test_cases = [
        "user@example.com",
        "invalid-email@",
        "another.valid@domain.org",
        "no-at-symbol.com",
        "user@domain"
    ]
    for address in test_cases:
        result = validator.validate(address)
        print(f"{address}: {result}")