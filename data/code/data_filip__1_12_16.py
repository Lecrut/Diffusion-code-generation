import re

EMAIL_PATTERN = re.compile(
    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
)

def validate_email(email: str) -> bool:
    return bool(EMAIL_PATTERN.match(email))

if __name__ == '__main__':
    test_addresses = [
        "user@example.com",
        "invalid.email@.com",
        "test.name@domain.co.uk",
        "@missing.local",
        "no-at-symbol.com",
        "user+tag@sub.domain.org"
    ]
    
    for address in test_addresses:
        print(validate_email(address))