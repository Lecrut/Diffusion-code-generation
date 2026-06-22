import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid.email@",
        "test.user+tag@domain.org",
        "@missinglocal.com",
        "spaces in@email.com",
        "valid.email@sub.domain.co.uk"
    ]
    results = [validate_email(email) for email in sample_emails]
    print(results)