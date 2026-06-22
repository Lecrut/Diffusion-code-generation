import re
import time

EMAIL_PATTERN = re.compile(
    r'^(?P<local>[a-zA-Z0-9_.+-]+)@'
    r'(?P<domain>[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*)$'
)

def validate_email(email):
    if not isinstance(email, str):
        return False
    return bool(EMAIL_PATTERN.match(email))

if __name__ == '__main__':
    test_cases = [
        ("user@example.com", True),
        ("user.name+tag@domain.co.uk", True),
        ("user_name-123@test.org", True),
        ("invalid.email@", False),
        ("@domain.com", False),
        ("user@.com", False),
        ("user@domain", True),
        ("user@domain.", False),
        ("user..name@domain.com", True),
        ("user@domain..com", False),
        ("user@domain.com ", False),
        (" user@domain.com", False),
        ("", False),
        ("user@ex ample.com", False),
        ("user@domain.c", True),
    ]

    for email, expected in test_cases:
        result = validate_email(email)
        print(f"{email!r}: {result} (expected: {expected})")

    valid_emails = [
        "a@b.co",
        "long_user@very_long_domain_name.com"
    ]
    
    if valid_emails:
        start_time = time.perf_counter()
        count = sum(1 for e in valid_emails if validate_email(e))
        end_time = time.perf_counter()
        print(f"Processed {count} valid emails in {end_time - start_time:.6f} seconds")