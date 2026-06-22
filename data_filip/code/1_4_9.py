import re

class EmailValidator:
    _pattern = re.compile(
        r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    )

    @staticmethod
    def is_valid(email):
        if not isinstance(email, str):
            return False
        return bool(EmailValidator._pattern.match(email))

if __name__ == '__main__':
    validator = EmailValidator()
    samples = [
        'valid.user@example.com',
        'invalid@.com',
        'missing-at-sign.com',
        'user@domain.org',
        'bad-email',
        'user+tag@sub.domain.co'
    ]
    for sample in samples:
        print(validator.is_valid(sample))