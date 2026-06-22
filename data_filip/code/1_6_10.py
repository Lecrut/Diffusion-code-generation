import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

def validate_email(email):
    return bool(EMAIL_REGEX.match(email))

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "john.doe@company.co.uk",
        "invalid@",
        "@invalid.com",
        "no-at-sign.com",
        "user@.com",
        "user@com.",
        "a@b.c",
        "valid.email+tag@sub.domain.org",
        "spaces in@email.com"
    ]
    for case in test_cases:
        print(f"{case}: {validate_email(case)}")