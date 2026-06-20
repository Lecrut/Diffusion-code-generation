import re
import sys

EMAIL_PATTERN = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

def is_valid_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    return bool(EMAIL_PATTERN.match(email))

if __name__ == '__main__':
    test_cases = ["user@example.com", "invalid-email@", "another@valid.co.uk", "@bad.com", "good.one@sub.domain.org"]
    results = [is_valid_email(case) for case in test_cases]
    for case, result in zip(test_cases, results):
        print(f"{case}: {result}")