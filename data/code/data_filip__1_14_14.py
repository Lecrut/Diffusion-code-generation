import re

_EMAIL_PATTERN = re.compile(
    r"^[a-zA-Z0-9]([a-zA-Z0-9._+-]*[a-zA-Z0-9])?@[a-zA-Z0-9]([a-zA-Z0-9.-]*[a-zA-Z0-9])?\.[a-zA-Z]{2,}$"
)

def check_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    if len(email) > 254:
        return False
    if email.startswith(".") or email.endswith("."):
        return False
    if ".." in email:
        return False
    if _EMAIL_PATTERN.match(email):
        domain_part = email.split("@")[-1]
        if domain_part.startswith("-") or domain_part.endswith("-"):
            return False
        return True
    return False

if __name__ == "__main__":
    test_emails = [
        "valid.email@example.com",
        "user+tag@sub.domain.org",
        "invalid.email@",
        "@missinglocal.com",
        "missingat.com",
        "double@@at.com",
        "spaces in email@test.com",
        "user.name@domain.co.uk",
        "a@b.c",
        "user@-invalid.com",
        "user@invalid-.com",
        ".invalid@start.com",
        "invalid.@end.com",
        "user..dots@domain.com",
        "normal@domain.com",
    ]
    results = [check_email(email) for email in test_emails]
    print(results)