import re

def validate_email(email):
    pattern = re.compile(
        r'^(?!.*\.\.)'
        r'[a-zA-Z0-9._%+-]+'
        r'@'
        r'(?!-)'
        r'[a-zA-Z0-9-]+'
        r'(?:\.[a-zA-Z0-9-]+)*'
        r'\.[a-zA-Z]{2,}$'
    )
    return bool(pattern.match(email))

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid.email@",
        "@missing.com",
        "user.name+tag@domain.co.uk",
        "bad..dot@domain.com",
        "no-at-sign.com",
        "user@domain",
        "test@sub.domain.org",
        "spaces@domain .com",
        "valid123@test-domain.com"
    ]
    results = [(email, validate_email(email)) for email in sample_emails]
    for email, is_valid in results:
        print(f"{email}: {is_valid}")