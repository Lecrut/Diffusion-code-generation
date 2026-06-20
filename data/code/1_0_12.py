import re

EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

def validate_email(email):
    if not isinstance(email, str):
        return False
    return EMAIL_PATTERN.match(email) is not None

def validate_emails(emails):
    return [validate_email(email) for email in emails]

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "invalid.email@.com",
        "another@domain.org",
        "@missing-local.com",
        "no-at-sign.com",
        "user@sub.domain.co.uk",
        "bad@@double.com",
        "spaces in@name.com",
        "valid.email+tag@provider.net",
        "a@b.co"
    ]
    results = validate_emails(test_emails)
    for email, is_valid in zip(test_emails, results):
        print(f"{email}: {is_valid}")