import re

VALID_EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

def validate_email(email):
    return bool(VALID_EMAIL_PATTERN.match(email))

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "invalid-email@",
        "@missing-local.com",
        "user.name+tag@domain.co.uk",
        "bad spaces@email.com",
        "a@b.c"
    ]
    results = [validate_email(email) for email in test_emails]
    print(results)