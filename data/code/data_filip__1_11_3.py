import re

def validate_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "invalid.email",
        "user@.com",
        "user@domain.co.uk",
        "another.user+tag@sub.domain.org",
        "@missinglocal.com",
        "user@domain",
        "user name@example.com"
    ]
    results = {email: validate_email(email) for email in test_emails}
    print(results)