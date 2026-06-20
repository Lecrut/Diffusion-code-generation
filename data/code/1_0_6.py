import re

EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

def validate_email_addresses(emails):
    results = {}
    for email in emails:
        if EMAIL_PATTERN.match(email):
            domain_part = email.split('@')[1]
            results[email] = domain_part
        else:
            results[email] = False
    return results

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "first.last@sub.domain.co.uk",
        "invalid-email@",
        "@missing-local.com",
        "no-at-sign.com",
        "user+tag@domain.org",
        "bad..dots@domain.com",
        "valid@123.45"
    ]
    validation_results = validate_email_addresses(test_emails)
    for email, result in validation_results.items():
        print(f"{email}: {result}")