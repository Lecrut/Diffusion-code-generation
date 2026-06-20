import re

def validate_emails(emails):
    pattern = re.compile(
        r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    )
    results = {}
    for email in emails:
        results[email] = bool(pattern.match(email))
    return results

if __name__ == '__main__':
    sample_emails = [
        'user@example.com',
        'invalid.email',
        'user@.com',
        'user@com.',
        '@example.com',
        'user name@example.com',
        'user@exam ple.com',
        'valid.email+tag@domain.co.uk',
        'a@b.cd',
        '123@456.789'
    ]
    validation_results = validate_emails(sample_emails)
    print(validation_results)