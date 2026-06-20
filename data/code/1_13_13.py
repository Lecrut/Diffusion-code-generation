import re

EMAIL_REGEX = re.compile(
    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
)

def validate_emails(emails):
    return [bool(EMAIL_REGEX.match(email)) for email in emails]

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid.email@",
        "another@domain.org",
        "@missinglocal.com",
        "no-at-sign.com",
        "valid+tag@sub.domain.co.uk",
        "spaces in@email.com",
        "user@.com",
        "user@domain.c",
        "good@email.info"
    ]
    results = validate_emails(sample_emails)
    print(results)