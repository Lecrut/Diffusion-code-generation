import re
import socket

def is_valid_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    if len(email) > 254:
        return False
    if not re.match(r"^[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}$", email):
        return False
    try:
        local_part, domain = email.rsplit('@', 1)
        if len(local_part) > 64:
            return False
        if len(domain) > 255:
            return False
        socket.gethostbyname(domain)
        return True
    except (ValueError, socket.gaierror, socket.herror, socket.timeout, OSError):
        return False

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "invalid.email",
        "user@nonexistentdomain12345.com",
        "user.name@sub.domain.co.uk",
        "@missinglocal.com",
        "missing@domain",
        "user@.com",
        "user@@domain.com"
    ]
    for case in test_cases:
        print(is_valid_email(case))