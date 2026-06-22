import re

_email_regex = re.compile(
    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
)

def validate_email(email):
    if not isinstance(email, str):
        return False
    return bool(_email_regex.match(email))

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "john.doe+tag@subdomain.example.co.uk",
        "invalid.email",
        "user@.com",
        "@missing-local.com",
        "spaces in@domain.com",
        "user@domain.",
        "",
        "a@b.c",
        "user name@example.com"
    ]
    results = []
    for email in test_cases:
        results.append((email, validate_email(email)))
    print(results)