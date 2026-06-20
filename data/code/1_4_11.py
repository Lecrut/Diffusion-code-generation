import re

class EmailValidator:
    _email_pattern = re.compile(
        r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    )

    @staticmethod
    def validate(email: str) -> bool:
        return bool(EmailValidator._email_pattern.match(email))

if __name__ == "__main__":
    test_emails = [
        "user@example.com",
        "invalid.email",
        "another.test@domain.co.uk",
        "@missing-local.com",
        "no-at-sign.com",
        "user@.com",
        "valid.email+tag@sub.domain.org"
    ]
    validator = EmailValidator()
    for email in test_emails:
        result = validator.validate(email)
        print(result)