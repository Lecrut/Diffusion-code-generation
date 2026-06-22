import re

EMAIL_REGEX = re.compile(
    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
)

def validate_email(email):
    if not isinstance(email, str):
        return False
    return bool(EMAIL_REGEX.match(email))

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid@",
        "user.name@domain.co.uk",
        "@missing-local.com",
        "user@.com",
        "valid.email+tag@sub.domain.org",
        "",
        "spaces not allowed@domain.com",
        "user@domain",
        "user@domain.c"
    ]
    for email in sample_emails:
        print(validate_email(email))