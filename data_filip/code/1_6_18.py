import re

email_pattern = re.compile(
    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
)

def validate_email(email):
    return bool(email_pattern.match(email))

if __name__ == '__main__':
    valid_emails = [
        "user@example.com",
        "first.last@domain.org",
        "user+tag@sub.domain.co.uk",
        "name123@test.io",
        "a@b.cd"
    ]
    invalid_emails = [
        "plainaddress",
        "@missing-local.com",
        "missing-at-sign.com",
        "two@@ats.com",
        "spaces in@name.com",
        "user@.invalid.com",
        "user@domain.",
        "user@domain.c",
        "user name@domain.com",
        ""
    ]
    for email in valid_emails:
        print(validate_email(email))
    for email in invalid_emails:
        print(validate_email(email))