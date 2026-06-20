import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid.email@",
        "test@domain.org",
        "@missinguser.com",
        "user@.com",
        "valid.email+tag@sub.domain.co.uk",
        "spaces in@email.com",
        "user@domain",
        "user@domain.c",
        "a@b.cc"
    ]
    for email in sample_emails:
        result = validate_email(email)
        print(result)