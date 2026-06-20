import re

def validate_email(email):
    if not isinstance(email, str):
        return False
    pattern = r'^[a-zA-Z0-9._%+-]+@(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid-email@",
        "test.user@domain.org",
        "@missing-local.com",
        "another@sub.domain.co.uk",
        "spaces in@email.com",
        "valid123@test.net"
    ]
    for email in sample_emails:
        print(validate_email(email))