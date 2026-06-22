import re

def validate_email(email):
    pattern = re.compile(r"""
        ^
        (?=.*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$)
        [a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}
        $
        """, re.VERBOSE)
    return bool(pattern.match(email))

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid-email@",
        "another.email+tag@domain.co.uk",
        "@missing-local.com",
        "no-at-sign.com",
        "user@.invalid",
        "user@domain."
    ]
    results = [validate_email(email) for email in sample_emails]
    print(results)