import re

EMAIL_REGEX = re.compile(
    r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
)

def validate_email(email):
    return bool(EMAIL_REGEX.match(email))

if __name__ == '__main__':
    samples = [
        "user@example.com",
        "invalid-email",
        "another.email@domain.org",
        "@missing-local.com",
        "no-at-sign.com",
        "user@.invalid",
        "valid+tag@sub.domain.co.uk"
    ]
    for sample in samples:
        print(validate_email(sample))