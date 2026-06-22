import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "invalid.email@",
        "@missing-local.com",
        "user@.com",
        "user@com",
        "valid.email+tag@domain.co.uk",
        "spaces in@email.com",
        "user@domain.c",
        "user@domain",
        "user@-domain.com",
        "user@domain-.com",
        ".user@domain.com",
        "user.@domain.com"
    ]
    results = [validate_email(email) for email in test_emails]
    for email, result in zip(test_emails, results):
        print(f"{email}: {result}")