import re
import time

_EMAIL_PATTERN = re.compile(
    r'^(?P<local>[a-zA-Z0-9_.+-]+)@'
    r'(?P<domain>[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*)$'
)

def validate_email(email):
    return _EMAIL_PATTERN.match(email) is not None

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "user.name+tag@domain.co.uk",
        "invalid-email@",
        "@missing-local.com",
        "no-at-sign.com",
        "spaces in@email.com",
        "user@sub.domain.org",
        "a@b.c",
        "user@domain",
        "user@-domain.com",
        "user@domain-.com"
    ]
    
    results = {}
    start_time = time.perf_counter()
    for email in test_cases:
        results[email] = validate_email(email)
    end_time = time.perf_counter()
    
    for email, is_valid in results.items():
        print(f"{email}: {is_valid}")
    print(f"Processed {len(test_cases)} emails in {end_time - start_time:.6f} seconds")