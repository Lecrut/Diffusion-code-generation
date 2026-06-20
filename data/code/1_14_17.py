import re

def is_valid_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.fullmatch(pattern, email) is not None

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "first.last@domain.org",
        "user+tag@domain.co.uk",
        "invalid-email",
        "no-at-sign.com",
        "@missing-local.com",
        "space @domain.com",
        "user@.com",
        "user@domain",
        "user@domain.c",
        "valid123@test-domain.net",
        "invalid..email@test.com"
    ]
    
    for email in test_emails:
        result = is_valid_email(email)
        print(f"{email}: {result}")