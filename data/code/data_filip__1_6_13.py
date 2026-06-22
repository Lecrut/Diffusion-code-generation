import re

def validate_emails(email_list):
    pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return [pattern.match(email) is not None for email in email_list]

if __name__ == '__main__':
    test_emails = [
        'valid@example.com',
        'user.name+tag@domain.co.uk',
        'invalid@.com',
        'no-at-sign.com',
        'missing-tld@domain',
        'double@@at.com',
        'spaces in@email.com',
        'user@domain.123',
        'simple@test.org',
        'a@b.cd'
    ]
    results = validate_emails(test_emails)
    for email, is_valid in zip(test_emails, results):
        print(f"{email}: {is_valid}")