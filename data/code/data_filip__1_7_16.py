import re

def is_valid_email(email: str) -> bool:
    pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return bool(pattern.match(email))

if __name__ == '__main__':
    samples = [
        "user@example.com",
        "invalid-email",
        "user.name+tag@domain.co.uk",
        "@missing-local.com",
        "no-at-sign.com",
        "user@.com",
        "user@domain.",
        "valid123@test-domain.org",
        "",
        "spaces in@email.com"
    ]
    results = [is_valid_email(sample) for sample in samples]
    print(list(zip(samples, results)))