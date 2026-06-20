import re

_EMAIL_REGEX = re.compile(
    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
)

def is_valid_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    if len(email) > 254:
        return False
    return bool(_EMAIL_REGEX.match(email))

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "user.name+tag@domain.co.uk",
        "invalid-email@",
        "@missing-local.com",
        "user@missing-tld",
        "spaces in@email.com",
        "valid_123@test.org"
    ]
    
    results = []
    for case in test_cases:
        results.append((case, is_valid_email(case)))
    
    for email, is_valid in results:
        print(f"{email}: {is_valid}")