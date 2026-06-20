import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

def validate_email(address):
    return bool(EMAIL_REGEX.match(address))

def validate_emails_batch(email_list):
    return [validate_email(addr) for addr in email_list]

if __name__ == '__main__':
    samples = [
        "valid@example.com",
        "user.name+tag@domain.co.uk",
        "invalid@.com",
        "@missing-local.com",
        "no-at-sign.com",
        "spaces @example.com",
        "double..dot@example.com",
        "valid123@test.org",
        "a@b.cc",
        "user@domain"
    ]
    print(validate_emails_batch(samples))