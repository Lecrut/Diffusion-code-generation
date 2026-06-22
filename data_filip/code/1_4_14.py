import re

class EmailValidator:
    email_pattern = re.compile(
        r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    )

    @staticmethod
    def validate(email):
        return bool(EmailValidator.email_pattern.match(email))

if __name__ == '__main__':
    validator = EmailValidator()
    print(validator.validate('user@example.com'))
    print(validator.validate('invalid-email'))
    print(validator.validate('another.user@domain.org'))