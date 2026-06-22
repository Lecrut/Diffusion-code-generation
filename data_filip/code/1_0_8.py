import re

EMAIL_REGEX = re.compile(
    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
)

def validate_email(email):
    return bool(EMAIL_REGEX.match(email))

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "invalid-email@",
        "test.user+tag@domain.co.uk",
        "@missing-local.com",
        "spaces in@email.com",
        "valid123@sub.domain.org",
        "no-at-sign.com",
        "a@b"
    ]
    
    results = [validate_email(email) for email in test_emails]
    print(results)