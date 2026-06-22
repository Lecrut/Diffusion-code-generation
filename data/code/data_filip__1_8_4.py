import re

_email_regex = re.compile(
    r"^(?P<local>[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+)"
    r"@"
    r"(?P<domain>(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+"
    r"[a-zA-Z]{2,})$"
)

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    if not email or len(email) > 254:
        return False
    if email.startswith(".") or email.endswith(".") or ".." in email:
        return False
    parts = email.split("@")
    if len(parts) != 2:
        return False
    local, domain = parts
    if not local or len(local) > 64:
        return False
    if domain.startswith(".") or domain.endswith("."):
        return False
    return bool(_email_regex.match(email))

if __name__ == "__main__":
    test_emails = [
        "user@example.com",
        "user.name+tag@sub.domain.co.uk",
        "invalid@domain",
        "@missinglocal.com",
        "missingdomain@",
        "double..dot@test.com",
        "too-long-local-part-" + "a" * 60 + "@test.com",
        "valid@test.co",
        "spaces in@email.com",
    ]
    for test_email in test_emails:
        print(validate_email(test_email))