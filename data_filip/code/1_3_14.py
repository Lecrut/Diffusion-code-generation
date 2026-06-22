import re

_EMAIL_PATTERN = re.compile(
    r"^(?:"
    r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*"
    r'|"(?:[\x01-\x08\x0B\x0C\x0E-\x1F\x21\x23-\x5B\x5D-\x7F]|\\[\x01-\x09\x0B\x0C\x0E-\x7F])*"'
    r")@(?:"
    r"(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
    r"|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\]"
    r"]$"
)

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    return bool(_EMAIL_PATTERN.fullmatch(email))

if __name__ == '__main__':
    results = [
        validate_email("valid.email@example.com"),
        validate_email("invalid@.com"),
        validate_email("test+tag@domain.co.uk"),
        validate_email('"quoted"@domain.com'),
        validate_email("no-at-sign"),
        validate_email("@missing.com"),
        validate_email("spaces in@domain.com")
    ]
    print(results)