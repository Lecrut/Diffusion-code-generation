import re

EMAIL_PATTERN = re.compile(
    r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
)

def validate_email(email: str) -> bool:
    return bool(EMAIL_PATTERN.match(email))

if __name__ == '__main__':
    valid_tests = [
        "user@example.com",
        "first.last@domain.org",
        "email@sub.domain.com",
        "user+tag@domain.co",
        "user_name@domain.museum"
    ]
    
    invalid_tests = [
        "plainaddress",
        "@missing.com",
        "missing@",
        "spaces in@email.com",
        "user@.com",
        "user@domain",
        ".user@domain.com",
        "user.@domain.com"
    ]
    
    valid_results = [validate_email(email) for email in valid_tests]
    invalid_results = [validate_email(email) for email in invalid_tests]
    
    print(f"Valid tests: {valid_results}")
    print(f"Invalid tests: {invalid_results}")