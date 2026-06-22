import re

def validate_emails(emails):
    pattern = re.compile(
        r'^(?:[a-z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+/=?^_`{|}~-]+)*|'
        r'"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")'
        r'@'
        r'(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$'
    )
    results = []
    for email in emails:
        results.append(bool(pattern.match(email)))
    return results

if __name__ == '__main__':
    samples = [
        "user@example.com",
        "invalid.email",
        "user@.com",
        "user_name@domain.co.uk",
        "plainaddress",
        "@missing.com",
        "user@domain",
        "quoted\"user\"@example.com",
        "user+tag@example.org",
        "user..name@example.com",
        "user@sub.domain.com",
        "user@localhost",
        "1234567890@example.com",
        "user@-invalid.com",
        "user@invalid-.com"
    ]
    print(validate_emails(samples))