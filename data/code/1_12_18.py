import re

EMAIL_PATTERN = re.compile(
    r'^(?P<local>[a-zA-Z0-9_.+-]+)@'
    r'(?P<domain>[a-zA-Z0-9-]+\.'
    r'[a-zA-Z0-9-.]+)$'
)

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    return EMAIL_PATTERN.match(email) is not None

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "invalid.email@",
        "another@valid-domain.org",
        "no_at_symbol.com",
        "spaces in email @domain.com",
        "correct.name+tag@sub.domain.co.uk"
    ]
    results = []
    for case in test_cases:
        results.append(validate_email(case))
    print(results)