import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

def validate_email(email):
    if not isinstance(email, str):
        return False
    return bool(EMAIL_REGEX.match(email))

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid.email@",
        "user@.com",
        "test.user+tag@domain.co.uk",
        "",
        "user name@example.com",
        "user@exam ple.com"
    ]
    for email in sample_emails:
        print(validate_email(email))