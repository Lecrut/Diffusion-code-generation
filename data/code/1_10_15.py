import re
import hashlib

_PATTERN = re.compile(
    r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
)

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    length = len(email)
    if length < 2 or length > 254:
        return False
    if email[0] == '.' or email[-1] == '.':
        return False
    if '..' in email:
        return False
    return bool(_PATTERN.match(email))

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "plainaddress",
        "@missing.com",
        "no-at-sign.com",
        "user@.com",
        "user@com.",
        "user@sub.domain.com",
        "user+tag@domain.co.uk",
        "user.name+tag@domain.com",
        "",
        "a@b",
        "user@[127.0.0.1]",
        "user name@domain.com",
        "user@domain com",
    ]

    expected_results = [
        True,
        False,
        False,
        False,
        False,
        False,
        True,
        True,
        True,
        False,
        True,
        False,
        False,
        False,
    ]

    results = []
    for email, expected in zip(test_emails, expected_results):
        actual = validate_email(email)
        results.append((email, expected, actual))

    output_lines = []
    for email, expected, actual in results:
        status = "PASS" if actual == expected else "FAIL"
        output_lines.append(f"{email!r}: {status} (expected={expected}, got={actual})")
    
    for line in output_lines:
        print(line)

    valid_count = sum(1 for _, _, actual in results if actual)
    invalid_count = sum(1 for _, _, actual in results if not actual)
    print(f"Total Valid: {valid_count}")
    print(f"Total Invalid: {invalid_count}")

    sample_hash = hashlib.sha256("user@example.com".encode()).hexdigest()
    print(f"Hash of valid sample: {sample_hash}")