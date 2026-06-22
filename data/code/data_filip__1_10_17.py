import re

_EMAIL_PATTERN = re.compile(
    r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
)

def validate_email(email):
    return bool(_EMAIL_PATTERN.match(email))

if __name__ == '__main__':
    valid_emails = ["user@example.com", "first.last@domain.co.uk", "user+tag@sub.domain.org"]
    invalid_emails = ["", "user@", "@domain.com", "user@.com", "user@domain", "user name@domain.com"]

    for email in valid_emails:
        print(validate_email(email))

    for email in invalid_emails:
        print(validate_email(email))