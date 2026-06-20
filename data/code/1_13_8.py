import re

def validate_email(emails: list) -> list:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    compiled_pattern = re.compile(pattern)
    results = []
    for email in emails:
        if isinstance(email, str) and len(email) > 0 and len(email) <= 254:
            results.append(bool(compiled_pattern.match(email)))
        else:
            results.append(False)
    return results

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid-email",
        "@missing-local.com",
        "local@.com",
        "local@com",
        "user+tag@example.co.uk",
        "user.name+tag@example.com",
        "user_name@example.org",
        "user-name@example.org",
        "user@sub.domain.com",
        "plainaddress",
        "@missing-domain.com",
        "user@",
        "user@domain",
        "user @domain.com",
        "user@domain .com",
        "user@domain..com",
        "user@domain.c",
        "user@domain.com.",
        ".user@example.com",
        "user.@example.com",
        "user..name@example.com",
        "user@.example.com",
        "user@example.com.",
        "u@bcdf"
    ]
    print(validate_email(sample_emails))