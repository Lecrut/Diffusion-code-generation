import re

EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9.!#$%&\'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$')

def validate_email(email):
    if not isinstance(email, str):
        return False
    return EMAIL_PATTERN.match(email) is not None

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "invalid.email@",
        "@missing-local.com",
        "user.name+tag@domain.co.uk",
        "spaces in@email.com",
        "user@.com",
        "user@domain",
        "a@b.c",
        "user@domain..com",
        "plainaddress"
    ]
    for email in test_emails:
        print(validate_email(email))