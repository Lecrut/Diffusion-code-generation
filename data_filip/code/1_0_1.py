import re
import socket

EMAIL_PATTERN = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

def validate_email(email):
    if not isinstance(email, str) or not email:
        return False
    if not EMAIL_PATTERN.match(email):
        return False
    try:
        local_part, domain = email.rsplit("@", 1)
        if not local_part or not domain:
            return False
        if local_part.startswith(".") or local_part.endswith(".") or ".." in local_part:
            return False
        socket.gethostbyname(domain)
        return True
    except (socket.gaierror, ValueError):
        return False

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "user.name+tag@domain.co.uk",
        "invalid-email@",
        "@missinglocal.com",
        "user@invalid-domain",
        "user@sub.domain.com",
        "user..double@domain.com",
        "valid.user_123@test-site.org"
    ]
    results = {email: validate_email(email) for email in test_emails}
    for email, is_valid in results.items():
        print(f"{email}: {is_valid}")