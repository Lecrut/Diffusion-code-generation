import re

class EmailValidator:
    email_pattern = re.compile(
        r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    )

    @staticmethod
    def validate(email):
        if not isinstance(email, str):
            return False
        return bool(EmailValidator.email_pattern.match(email))

if __name__ == '__main__':
    validator = EmailValidator()
    test_emails = [
        'user@example.com',
        'invalid.email',
        'user@.com',
        '@example.com',
        'user@exam ple.com',
        'valid.email+tag@domain.co.uk',
    ]
    for email in test_emails:
        print(validator.validate(email))