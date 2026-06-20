import re

def validate_email(email: str) -> bool:
    pattern = re.compile(
        r"^(?=[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$)"
        r"(?=[^@]*$)"
        r"^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    )
    return pattern.match(email) is not None

def get_domain(email: str) -> str:
    if "@" in email:
        return email.split("@")[-1]
    return ""

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid.email@",
        "another.user@sub.domain.org",
        "@missing-local.com",
        "no-at-sign.com"
    ]

    for email in sample_emails:
        is_valid = validate_email(email)
        domain = get_domain(email)
        print(f"{email}: valid={is_valid}, domain={domain}")