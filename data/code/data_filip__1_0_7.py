import re

EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

def validate_emails(email_list):
    results = []
    for email in email_list:
        results.append(bool(EMAIL_PATTERN.match(email)))
    return results

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "invalid.email",
        "test@sub.domain.co.uk",
        "@nodomain.com",
        "no-at-sign.org",
        "user@.invalid",
        "user@invalid..com"
    ]
    valid_results = validate_emails(test_emails)
    print(valid_results)