import re
import sys

_EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    if not email:
        return False
    return bool(_EMAIL_PATTERN.match(email))

if __name__ == '__main__':
    samples = [
        "user@example.com",
        "invalid.email@",
        "user@domain",
        "test+tag@sub.domain.org",
        "another@test.co.uk",
        "@missing.local",
        "no-at-sign.com"
    ]
    for sample in samples:
        print(f"{sample}: {validate_email(sample)}")