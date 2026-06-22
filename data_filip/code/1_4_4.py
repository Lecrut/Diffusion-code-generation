import re

class EmailValidator:
    @staticmethod
    def validate(email_address):
        if not isinstance(email_address, str):
            return False
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(pattern, email_address))

if __name__ == '__main__':
    validator = EmailValidator()
    test_email_1 = "user@example.com"
    test_email_2 = "invalid.email@.com"
    print(validator.validate(test_email_1))
    print(validator.validate(test_email_2))