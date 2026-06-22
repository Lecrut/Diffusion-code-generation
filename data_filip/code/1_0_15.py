import re

EMAIL_PATTERN = re.compile(
    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
)

def validate_email(email):
    if not isinstance(email, str):
        return False
    return bool(EMAIL_PATTERN.match(email))

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "invalid@.com",
        "@missing-local.com",
        "no-at-sign.com",
        "user@sub.domain.co.uk",
        "spaces in@name.com",
        "user@domain.",
        ".leading-dot@domain.com",
        "trailing-dot.@domain.com",
        "user+tag@domain.org"
    ]
    results = [validate_email(email) for email in test_emails]
    print(results)