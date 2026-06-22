import re

class EmailValidator:
    @staticmethod
    def validate(email):
        if not isinstance(email, str):
            return False
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))

if __name__ == '__main__':
    validator = EmailValidator()
    test_emails = ["user@example.com", "invalid.email@", "@missing.com", "valid.user@domain.org"]
    for email in test_emails:
        result = validator.validate(email)
        print(f"{email}: {result}")