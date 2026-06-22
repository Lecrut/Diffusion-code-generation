import re

def validate_email(email):
    if not isinstance(email, str):
        return False
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.fullmatch(pattern, email))

if __name__ == "__main__":
    samples = [
        "user@example.com",
        "user.name+tag@domain.co.uk",
        "invalid-email@",
        "@missing-user.com",
        "no-at-symbol.com",
        "valid_user-123@test.org"
    ]
    for s in samples:
        result = validate_email(s)
        print(f"{s}: {result}")