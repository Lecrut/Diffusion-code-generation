import re

_email_regex = re.compile(
    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
)

def validate_email(email):
    return bool(_email_regex.match(email))

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid.email@.com",
        "user.name+tag@domain.co.uk",
        "@missinglocal.com",
        "nodomaint.com",
        "user@domain",
        "spaces in@domain.com",
        "valid123@sub.domain.org"
    ]
    for email in sample_emails:
        result = validate_email(email)
        print(result)