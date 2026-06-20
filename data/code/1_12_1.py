import re

EMAIL_REGEX = re.compile(
    r'^(?!.*\.\.)[a-zA-Z0-9.!#$%&*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}$'
)

def validate_email(email):
    if not isinstance(email, str):
        return False
    return bool(EMAIL_REGEX.match(email))

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid-email@.com",
        "test.user@domain.co.uk",
        "bad@@domain.com",
        "user@domain.c",
        "another@valid-domain.org",
        "no_at_sign.com",
        "spaces in@email.com",
        "valid+tag@gmail.com"
    ]
    results = [validate_email(email) for email in sample_emails]
    print(dict(zip(sample_emails, results)))