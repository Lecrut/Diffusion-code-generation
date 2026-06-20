import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.!#$%&\'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$')

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    if len(email) > 254:
        return False
    local_parts = email.split('@')
    if len(local_parts) != 2:
        return False
    local_part, domain_part = local_parts
    if len(local_part) == 0 or len(local_part) > 64:
        return False
    if len(domain_part) == 0 or len(domain_part) > 253:
        return False
    return bool(EMAIL_REGEX.match(email))

def validate_email_list(emails: list) -> dict:
    results = {}
    for email in emails:
        results[email] = validate_email(email)
    return results

if __name__ == '__main__':
    sample_emails = [
        "normal@domain.com",
        "invalid@",
        "@missing.com",
        "no_at_symbol.com",
        "user.name+tag@sub.domain.co.uk",
        "simple@example.org",
        "invalid..double..dot@domain.com",
        "user@domain",
        "user@-invalid.com",
        "user@domain.c",
        "spaces in@domain.com",
        "user@domain..com",
        "",
        "user@domain.com.",
        "user..name@domain.com"
    ]
    print(validate_email_list(sample_emails))