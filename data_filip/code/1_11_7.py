import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "user.name@domain.co.uk",
        "invalid-email@",
        "@missinglocal.com",
        "no-at-symbol.com",
        "user@domain",
        "user+tag@example.org"
    ]
    results = []
    for email in test_emails:
        results.append((email, validate_email(email)))
    for email, is_valid in results:
        print(f"{email}: {is_valid}")