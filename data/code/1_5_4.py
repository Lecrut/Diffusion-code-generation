import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    samples = [
        "user@example.com",
        "invalid.email@",
        "@missing-local.com",
        "user.name+tag@domain.co.uk",
        "spaces in@email.com",
        "no-at-sign.com",
        "user@.com",
        "user@domain.c",
        "valid.email-123@sub.domain.org",
        "",
        "a@b.c",
        "user@@domain.com"
    ]
    for sample in samples:
        result = validate_email(sample)
        print(f"{sample}: {result}")