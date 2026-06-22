import re

EMAIL_PATTERN = re.compile(
    r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
)

def is_valid_email(email: str) -> bool:
    return bool(EMAIL_PATTERN.match(email))

if __name__ == '__main__':
    valid_emails = [
        "user@example.com",
        "first.last@sub.domain.co.uk",
        "user+tag@domain.org",
        "1234567890@domain.com"
    ]

    invalid_emails = [
        "plainaddress",
        "@missinglocal.com",
        "user@.com",
        "user@domain",
        "user name@domain.com",
        "user@@domain.com"
    ]

    valid_results = [is_valid_email(email) for email in valid_emails]
    invalid_results = [is_valid_email(email) for email in invalid_emails]

    print(valid_results)
    print(invalid_results)