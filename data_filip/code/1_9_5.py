import re

EMAIL_PATTERN = re.compile(
    r'^[a-zA-Z0-9](?:[a-zA-Z0-9_.+-]*[a-zA-Z0-9])?@[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.'
    r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$'
)

def validate_email(email: str) -> bool:
    return EMAIL_PATTERN.match(email) is not None

if __name__ == '__main__':
    samples = [
        "user@example.com",
        "invalid.email",
        "@missing-local.com",
        "normal@address.org",
        "bad@.com",
        "valid+tag@example.co.uk"
    ]
    results = [validate_email(e) for e in samples]
    print(results)