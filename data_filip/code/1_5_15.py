import re
import ipaddress

_email_regex = re.compile(
    r"^(?![.])"
    r"[a-zA-Z0-9._%+-]+"
    r"@"
    r"(?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}"
    r"|(?:\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\]))"
    r"(?![.])$"
)

_invalid_domains = {
    "localhost",
    "example.com",
    "invalid.tld",
}

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False

    if not email or len(email) > 320:
        return False

    if ".." in email:
        return False

    at_index = email.rfind("@")
    if at_index < 1:
        return False

    local_part = email[:at_index]
    domain_part = email[at_index + 1:]

    if len(local_part) == 0 or len(local_part) > 64:
        return False

    if len(domain_part) == 0 or len(domain_part) > 253:
        return False

    if not _email_regex.match(email):
        return False

    if domain_part in _invalid_domains:
        return False

    if domain_part.startswith("[") and domain_part.endswith("]"):
        ip_str = domain_part[1:-1]
        try:
            ipaddress.IPv4Address(ip_str)
        except ipaddress.AddressValueError:
            return False

    return True

if __name__ == "__main__":
    test_emails = [
        "user@example.com",
        "first.last@domain.co.uk",
        "user+tag@sub.domain.org",
        "invalid@.com",
        "@missing.local",
        "no_at_sign.com",
        "spaces in@email.com",
        "user@-invalid.com",
        "user@192.168.1.1",
        "user@256.0.0.1",
    ]
    results = [validate_email(email) for email in test_emails]
    print(results)