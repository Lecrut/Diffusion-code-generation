import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

def validate_email_format(address):
    return bool(EMAIL_REGEX.match(address))

class EmailChecker:
    def __init__(self):
        self.pattern = EMAIL_REGEX

    def check(self, email_str):
        return bool(self.pattern.match(email_str))

    def validate_batch(self, emails):
        return {email: self.check(email) for email in emails}

if __name__ == '__main__':
    checker = EmailChecker()
    test_emails = [
        "john.doe@example.com",
        "jane+tag@domain.org",
        "invalid@.com",
        "missing_at_sign",
        "@no_local.com",
        "user@sub.domain.co.uk",
        "bad format@email.com",
        "test@domain"
    ]
    results = checker.validate_batch(test_emails)
    print(results)