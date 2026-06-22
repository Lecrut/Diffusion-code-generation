import re

EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

TEST_EMAILS = [
    "user@example.com",
    "invalid-email@.com",
    "name@subdomain.example.co.uk",
    "@missing-local.com",
    "spaces in@email.com",
    "normal+tag@domain.org"
]

def validate_emails(emails):
    results = []
    for email in emails:
        results.append(bool(EMAIL_PATTERN.match(email)))
    return results

if __name__ == '__main__':
    print(validate_emails(TEST_EMAILS))