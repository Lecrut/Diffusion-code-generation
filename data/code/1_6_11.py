import re

EMAIL_PATTERN = re.compile(
    r'^(?P<local>[a-zA-Z0-9._%+-]+)'
    r'@'
    r'(?P<domain>[a-zA-Z0-9.-]+)'
    r'\.(?P<tld>[a-zA-Z]{2,})$'
)

def is_valid_email(email):
    if not isinstance(email, str):
        return False
    if not EMAIL_PATTERN.match(email):
        return False
    return True

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "admin@sub.domain.org",
        "first.last+tag@company.co.uk",
        "invalid-email@",
        "@missing-local.com",
        "spaces in email@test.com",
        "no-at-sign.com",
        "double@@sign.com",
        "valid_underscore@domain-test.net",
        "UPPERCASE@CASESENSITIVE.COM"
    ]
    results = [is_valid_email(email) for email in test_cases]
    for email, is_valid in zip(test_cases, results):
        print(f"{email}: {is_valid}")