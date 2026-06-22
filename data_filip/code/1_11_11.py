import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    samples = [
        "user@example.com",
        "invalid@",
        "missing-at-sign.com",
        "user.name+tag@domain.co.uk",
        "@no-user.com",
        "spaces in@domain.com",
        "user@.com",
        "user@domain"
    ]
    results = [validate_email(s) for s in samples]
    print(results)