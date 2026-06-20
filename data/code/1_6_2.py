import re

_email_pattern = re.compile(
    r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
)

def validate_email(email):
    return bool(_email_pattern.match(email))

if __name__ == '__main__':
    valid_emails = [
        "user@example.com",
        "john.doe@company.org",
        "alice+tag@mail.co.uk",
        "name_123@test-domain.com",
        "user@sub.domain.example.com"
    ]
    invalid_emails = [
        "plainaddress",
        "@missing-local.com",
        "missing-at-sign.com",
        "user@.com",
        "user@.com",
        "spaces in@email.com",
        "user@domain.",
        "",
        "user@-domain.com",
        "user@domain-.com"
    ]

    results = {}
    for email in valid_emails:
        results[email] = validate_email(email)
    for email in invalid_emails:
        results[email] = validate_email(email)

    print(results)