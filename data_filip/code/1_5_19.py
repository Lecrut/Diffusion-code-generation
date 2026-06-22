import re
from typing import Optional

_EMAIL_PATTERN = re.compile(
    r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
)

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    if len(email) > 254:
        return False
    if len(email) < 5:
        return False
    if email.startswith(".") or email.endswith("."):
        return False
    if ".." in email:
        return False
    local_part, _, domain_part = email.rpartition("@")
    if not local_part or not domain_part:
        return False
    if len(local_part) > 64:
        return False
    if len(domain_part) > 253:
        return False
    if not re.match(r"^[a-zA-Z0-9.-]+$", domain_part):
        return False
    if domain_part.startswith("-") or domain_part.endswith("-"):
        return False
    if ".." in domain_part:
        return False
    domain_labels = domain_part.split(".")
    for label in domain_labels:
        if not label:
            return False
        if len(label) > 63:
            return False
        if label.startswith("-") or label.endswith("-"):
            return False
    return _EMAIL_PATTERN.match(email) is not None

if __name__ == "__main__":
    print(validate_email("user@example.com"))
    print(validate_email("invalid-email"))
    print(validate_email("@example.com"))
    print(validate_email("user@.com"))
    print(validate_email("user@domain..com"))