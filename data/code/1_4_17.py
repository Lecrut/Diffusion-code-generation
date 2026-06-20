import re

class EmailValidator:
    email_pattern = re.compile(
        r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    )

    @staticmethod
    def is_valid(email):
        return bool(EmailValidator.email_pattern.match(email))

if __name__ == '__main__':
    validator = EmailValidator()
    print(validator.is_valid('test@example.com'))
    print(validator.is_valid('invalid-email'))
    print(validator.is_valid('user.name+tag@domain.co.uk'))
    print(validator.is_valid('missing-at-sign.com'))
    print(validator.is_valid('@missing-local.com'))