import re

_EMAIL_PATTERN = re.compile(
    r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
)

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    if not email:
        return False
    if len(email) > 254:
        return False
    if "@" in email:
        local, domain = email.rsplit("@", 1)
    else:
        return False
    if not local or not domain:
        return False
    if "." not in domain:
        return False
    if domain.startswith(".") or domain.endswith("."):
        return False
    if ".." in domain:
        return False
    if _EMAIL_PATTERN.match(email):
        return True
    return False

if __name__ == "__main__":
    result = validate_email("user@example.com")
    print(result)