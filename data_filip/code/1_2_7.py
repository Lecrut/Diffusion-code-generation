import re

DOMAIN_PATTERN = re.compile(r"^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

def validate_email(email: str) -> bool:
    if not isinstance(email, str) or "@" not in email:
        return False
    parts = email.split("@")
    if len(parts) != 2:
        return False
    local_part, domain_part = parts
    if not local_part or not domain_part:
        return False
    if "@" in domain_part:
        return False
    if not DOMAIN_PATTERN.match(domain_part):
        return False
    return True

if __name__ == "__main__":
    print(validate_email("user@example.com"))
    print(validate_email("invalid.email@"))
    print(validate_email("no-at-symbol.com"))
    print(validate_email("multiple@@signs.com"))