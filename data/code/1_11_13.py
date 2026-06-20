import re

EMAIL_REGEX = re.compile(
    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
)

def validate_email(email):
    if not isinstance(email, str):
        return False
    return bool(EMAIL_REGEX.match(email))

if __name__ == '__main__':
    samples = [
        "user@example.com",
        "invalid.email@",
        "test.name+tag@domain.co.uk",
        "a@b.c",
        "",
        123,
        "hello world@example.com"
    ]
    results = [validate_email(s) for s in samples]
    for sample, result in zip(samples, results):
        print(f"{sample}: {result}")