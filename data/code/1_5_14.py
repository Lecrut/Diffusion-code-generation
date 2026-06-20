import re
import sys

_email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

def validate_email(email_str):
    if not isinstance(email_str, str):
        return False
    return bool(_email_pattern.match(email_str))

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid.email@",
        "another@valid-domain.org",
        "no_at_symbol.com",
        "bad..double@domain.com",
        12345,
        ""
    ]
    results = []
    for email in sample_emails:
        results.append(validate_email(email))
    print(results)