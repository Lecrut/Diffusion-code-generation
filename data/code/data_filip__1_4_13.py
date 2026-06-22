import re

class EmailValidator:
    @staticmethod
    def validate(email: str) -> bool:
        if not isinstance(email, str):
            return False
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None

if __name__ == '__main__':
    validator = EmailValidator()
    print(validator.validate("user@example.com"))
    print(validator.validate("invalid-email@"))
    print(validator.validate("another.user@domain.co.uk"))
    print(validator.validate("no-at-symbol.com"))