import re

def validate_email(address):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, address))

if __name__ == '__main__':
    test_cases = ["user@example.com", "invalid.email@", "no-at-symbol.com", "valid.name+tag@sub.domain.org"]
    for case in test_cases:
        print(f"{case}: {validate_email(case)}")