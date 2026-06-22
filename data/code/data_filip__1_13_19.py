import re

EMAIL_REGEX = re.compile(
    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
)

def validate_emails(emails):
    return [bool(EMAIL_REGEX.match(email)) for email in emails]

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid.email",
        "another@domain.org",
        "missing-at-sign.com",
        "@missing-local.com",
        "spaces in@email.com",
        "valid+tag@sub.domain.co.uk",
        "",
        "user@.com",
        "user@domain.",
        "a@b.c",
        "test@domain.com."
    ]
    print(validate_emails(sample_emails))