import re

def validate_email(email):
    pattern = re.compile(
        r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    )
    if not isinstance(email, str):
        return False
    return bool(pattern.match(email))

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid.email@",
        "another@invalid",
        "test.user+tag@domain.co.uk",
        "spaces in@email.com",
        "@missinglocal.com",
        "valid123@sub.domain.org"
    ]
    for email in sample_emails:
        result = validate_email(email)
        print(result)