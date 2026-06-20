import re

def validate_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.fullmatch(pattern, email))

def run_tests():
    test_cases = [
        ("user@example.com", True),
        ("first.last@sub.domain.org", True),
        ("email+tag@example.net", True),
        ("name_123@domain.co", True),
        ("plainaddress", False),
        ("@missing-local.com", False),
        ("missing@.com", False),
        ("missing@com", False),
        ("space in@email.com", False),
        ("double@@email.com", False),
        ("", False),
        ("user@domain", False),
    ]
    
    results = []
    for email, expected in test_cases:
        result = validate_email(email)
        results.append((email, result))
    return results

if __name__ == '__main__':
    for email, is_valid in run_tests():
        print(f"{email}: {is_valid}")