import re

def is_valid_email(email: str) -> bool:
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

if __name__ == "__main__":
    test_cases = [
        "user@example.com",
        "invalid-email@",
        "another@valid-domain.org",
        "bad..double@point.com"
    ]
    results = [is_valid_email(case) for case in test_cases]
    for case, result in zip(test_cases, results):
        print(f"{case}: {result}")