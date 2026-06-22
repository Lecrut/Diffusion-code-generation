import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_emails(emails):
    return [validate_email(email) for email in emails]

if __name__ == '__main__':
    sample_emails = [
        "valid@example.com",
        "invalid@",
        "@invalid.com",
        "no-at-sign.com",
        "user@domain",
        "another.email@domain.co.uk",
        "spaces in@email.com",
        "user@.com",
        "user@domain.",
        "a@b.c",
        "test.email+tag@domain.org",
        "invalid.email@",
        "",
        "user name@example.com",
        "user@domain..com"
    ]
    results = validate_emails(sample_emails)
    for email, is_valid in zip(sample_emails, results):
        print(f"{email}: {is_valid}")