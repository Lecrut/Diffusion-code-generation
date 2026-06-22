import re

EMAIL_REGEX = re.compile(
    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
)

def validate_email(email):
    return bool(EMAIL_REGEX.match(email))

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid.email@",
        "test.name+tag@domain.co.uk",
        "@missinglocal.com",
        "spaces in@email.com",
        "valid123@sub.domain.org"
    ]
    for email in sample_emails:
        print(validate_email(email))