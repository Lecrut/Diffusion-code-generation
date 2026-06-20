import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    samples = [
        "user@example.com",
        "invalid-email@.com",
        "another.valid+tag@domain.co.uk",
        "@missing-local.com",
        "no-at-sign.com",
        "spaces in@email.com"
    ]
    results = [is_valid_email(s) for s in samples]
    print(dict(zip(samples, results)))