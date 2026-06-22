import re
from typing import List, Tuple

_EMAIL_PATTERN = re.compile(
    r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
)

def validate_email(email: str) -> bool:
    return bool(_EMAIL_PATTERN.match(email))

def run_tests() -> List[Tuple[str, bool]]:
    test_cases: List[Tuple[str, bool]] = [
        ("user@example.com", True),
        ("john.doe+tag@domain.co.uk", True),
        ("plainaddress", False),
        ("@missinguser.com", False),
        ("missing@domain", False),
        ("missing@.com", False),
        ("user@domain..com", False),
        ("user name@domain.com", False),
        ("user@domain.com.", False),
        ("", False),
    ]
    results: List[Tuple[str, bool]] = []
    for email, expected in test_cases:
        result = validate_email(email)
        results.append((email, result))
    return results

if __name__ == "__main__":
    test_results = run_tests()
    print(test_results)