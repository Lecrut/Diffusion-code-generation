import re
import sys

_EMAIL_PATTERN = re.compile(
    r"^(?!\.)[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*\.[a-zA-Z]{2,}$"
)

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    if len(email) < 1 or len(email) > 254:
        return False
    if _EMAIL_PATTERN.match(email):
        return True
    return False

if __name__ == '__main__':
    results = [
        validate_email("user@example.com"),
        validate_email("invalid.email@"),
        validate_email("missing@domain"),
        validate_email("plainaddress"),
        validate_email("@missing.com"),
        validate_email("spaces in@email.com"),
        validate_email("valid+tag@sub.domain.co.uk"),
        validate_email("user.name+tag@long-domain-name.example.com"),
        validate_email(""),
        validate_email(12345),
    ]

    assertions = [
        results[0] is True,
        results[1] is False,
        results[2] is False,
        results[3] is False,
        results[4] is False,
        results[5] is False,
        results[6] is True,
        results[7] is True,
        results[8] is False,
        results[9] is False,
    ]

    if not all(assertions):
        sys.exit(1)

    print(results)