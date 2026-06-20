import re

class EmailValidator:
    @staticmethod
    def is_valid(email):
        if not isinstance(email, str):
            return False
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

if __name__ == '__main__':
    validator = EmailValidator()
    test_emails = [
        "user@example.com",
        "invalid-email@",
        "another.valid@domain.co.uk",
        "no-at-sign.com",
        "@missing-local-part.com"
    ]
    for email in test_emails:
        result = validator.is_valid(email)
        print(f"{email}: {result}")