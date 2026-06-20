import re

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    if len(email) > 254:
        return False
    if email.count('@') != 1:
        return False
    local, domain = email.split('@')
    if not local or not domain:
        return False
    if local.startswith('.') or local.endswith('.'):
        return False
    if '..' in local:
        return False
    if len(local) > 64:
        return False
    if len(domain) > 253:
        return False
    if domain.startswith('.') or domain.endswith('.'):
        return False
    if '..' in domain:
        return False
    domain_parts = domain.split('.')
    if any(len(part) > 63 or not part for part in domain_parts):
        return False
    if domain_parts[-1] == '':
        return False
    if not re.match(r"^[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+)*$", local):
        return False
    if not re.match(r"^[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", domain):
        return False
    return True

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "user.name+tag@example.co.uk",
        "invalid_email@",
        "@example.com",
        "user@.com",
        "user@domain..com",
        ".user@example.com",
        "user..name@example.com",
        "very.long.email.address.that.exceeds.the.maximum.allowed.length.of.sixty.four.characters.in.this.part@example.com",
        "user@toolongdomainnamethatexceedsthesixtythreecharacterlimitperlabel.example.com",
        "user@localhost"
    ]
    for email in test_cases:
        result = validate_email(email)
        print(f"{email}: {result}")