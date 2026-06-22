import re

_email_pattern = re.compile(
    r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
)

def validate_email(email: str) -> bool:
    return bool(_email_pattern.match(email))

if __name__ == "__main__":
    test_emails = [
        "user@example.com",
        "first.last@domain.co.uk",
        "user123@test-site.org",
        "invalid-email",
        "@missing-local.com",
        "missing-at.com",
        "double@@at.com",
        "spaces in@email.com",
        "user@.invalid.com",
        "user@invalid..com",
    ]
    results = [validate_email(email) for email in test_emails]
    print(results)