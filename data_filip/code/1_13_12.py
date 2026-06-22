import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_emails(emails):
    return [validate_email(email) for email in emails]

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid.email@",
        "@missinglocal.com",
        "user.name+tag@domain.co.uk",
        "spaces in@domain.com",
        "user@.invalid.com",
        "valid@sub.domain.org",
        "noatsign.com",
        "multiple@@signs.com",
        "user@domain"
    ]
    results = validate_emails(sample_emails)
    print(results)