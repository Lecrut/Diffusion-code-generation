import re

_EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

def validate_email(email: str) -> bool:
    return bool(_EMAIL_PATTERN.match(email))

if __name__ == '__main__':
    test_cases = [
        ("user@example.com", True),
        ("john.doe@company.org", True),
        ("invalid@.com", False),
        ("@missing-local.com", False),
        ("missing@domain", False),
        ("spaces in@email.com", False),
        ("simple@example.org", True),
        ("very.common@example.com", True),
        ("disposable.style.email.with+symbol@example.com", True),
        ("other.email-with-hyphen@example.com", True),
        ("fully-qualified-domain@example.com", True),
        ("user.name+tag+sorting@example.com", True),
        ("example-indeed@strange-example.com", True),
        ("example@s.example", True),
        ("user@localhost", False),
        ("user@.localhost", False),
        ("user@local.", False),
        ("user..name@example.com", False),
        ("user_name@example.com", True),
        ("user123@example.com", True),
        ("user@-example.com", False),
        ("user@example-.com", False),
        ("user@example.c", False),
        ("user@192.168.1.1", False),
        ("user@[192.168.1.1]", False),
        ("", False),
        ("email", False),
        ("@", False),
        ("@@", False),
        ("user@", False),
        ("@domain", False),
        ("user domain@example.com", False),
        ("user@@example.com", False),
        ("user@.com", False),
        ("user@example.com.", False),
        ("user@example..com", False),
    ]

    results = []
    for email, expected in test_cases:
        is_valid = validate_email(email)
        status = "PASS" if is_valid == expected else "FAIL"
        results.append({
            "email": email,
            "expected": expected,
            "actual": is_valid,
            "status": status
        })

    failures = [r for r in results if r["status"] == "FAIL"]
    if failures:
        print(failures)
    else:
        print(f"All {len(results)} tests passed.")
    print(results[-1])