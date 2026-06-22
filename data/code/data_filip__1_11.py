import re

EMAIL_REGEX = re.compile(
    r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
)

def validate_email(email):
    return bool(EMAIL_REGEX.match(email))

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid.email",
        "another.user@domain.co.uk",
        "@missing-local.com",
        "missing-domain@",
        "user.name+tag@example-domain.org"
    ]
    for email in sample_emails:
        print(validate_email(email))