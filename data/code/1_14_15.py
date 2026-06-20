import re

EMAIL_REGEX = re.compile(
    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
)

def validate_email(email):
    if not isinstance(email, str):
        return False
    return EMAIL_REGEX.match(email) is not None

def run_tests():
    test_cases = [
        ("user@example.com", True),
        ("john.doe@company.co.uk", True),
        ("alice+tag@domain.org", True),
        ("invalid@", False),
        ("@missing-local.com", False),
        ("no-at-sign.com", False),
        ("spaces in@email.com", False),
        ("user@.com", False),
        ("user@domain.", False),
        ("user name@domain.com", False),
        ("", False),
        ("user@domain", False),
        ("valid.email@sub.domain.com", True),
        ("a@b.cc", True),
        ("x@y.z", False),
    ]
    results = []
    for email, expected in test_cases:
        result = validate_email(email)
        results.append((email, expected, result))
    return results

if __name__ == '__main__':
    test_results = run_tests()
    for email, expected, actual in test_results:
        print(f"validate_email({email!r}) -> {actual} (expected: {expected})")