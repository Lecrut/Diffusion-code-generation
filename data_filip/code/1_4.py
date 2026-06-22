import re

class EmailValidator:
    _email_pattern = re.compile(
        r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    )

    @staticmethod
    def validate(email):
        return bool(EmailValidator._email_pattern.match(email))

if __name__ == '__main__':
    validator = EmailValidator()
    sample_emails = [
        'user@example.com',
        'invalid-email@',
        'another.user+tag@domain.co.uk',
        '@missing-local.com',
        'no-at-sign.com',
        'spaces in@email.com',
        'valid123@sub.domain.org'
    ]
    results = [validator.validate(email) for email in sample_emails]
    for email, is_valid in zip(sample_emails, results):
        print(f"{email}: {is_valid}")