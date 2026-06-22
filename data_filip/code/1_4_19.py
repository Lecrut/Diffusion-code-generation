import re

class EmailValidator:
    EMAIL_REGEX = re.compile(
        r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    )

    @staticmethod
    def validate(email):
        return bool(EmailValidator.EMAIL_REGEX.match(email))

if __name__ == '__main__':
    validator = EmailValidator()
    sample_emails = [
        "user@example.com",
        "invalid-email@",
        "test.name+tag@domain.co.uk",
        "@missing-local.com",
        "no-at-sign.com",
        "spaces in@email.com"
    ]
    results = [validator.validate(email) for email in sample_emails]
    for email, is_valid in zip(sample_emails, results):
        print(f"{email}: {is_valid}")