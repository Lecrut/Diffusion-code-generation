import re

def validate_email(email):
    pattern = (
        r'^(?!.*\.\.)(?!.*\.$)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    )
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    samples = [
        "user@example.com",
        "invalid.email@.com",
        "test@domain.co.uk",
        "bad@domain",
        "another..dot@test.org",
        "valid+tag@gmail.com"
    ]
    results = [validate_email(email) for email in samples]
    print(results)