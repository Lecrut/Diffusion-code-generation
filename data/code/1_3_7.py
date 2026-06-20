import re

_LOCAL_ATOM_CHAR = r"[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]"
_DOT_ATOM = r"(?:" + _LOCAL_ATOM_CHAR + r"+\.)*" + _LOCAL_ATOM_CHAR + r"+"
_QUOTED_PAIR = r"\\[\x00-\x7F]"
_QUOTED_STRING = r'"(?:' + _QUOTED_PAIR + r'|[^"\\])*"'
_LOCAL_PART = r"(?:" + _DOT_ATOM + r"|" + _QUOTED_STRING + r")"
_DTEXT = r"[\x21-\x5B\x5D-\x7E]"
_DOMAIN_LITERAL = r"\[(?:" + _DTEXT + r"|" + _QUOTED_PAIR + r")*\]"
_DOMAIN_ATOM = r"[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?"
_DOMAIN_ATOM_DOT = r"(?:" + _DOMAIN_ATOM + r"\.)+" + _DOMAIN_ATOM
_DOMAIN = r"(?:" + _DOMAIN_ATOM_DOT + r"|" + _DOMAIN_LITERAL + r")"
_RFC5322_PATTERN = re.compile(r"^" + _LOCAL_PART + r"@" + _DOMAIN + r"$")

class EmailValidator:
    def __init__(self):
        self._pattern = _RFC5322_PATTERN

    def validate(self, address):
        return bool(self._pattern.match(address))

if __name__ == '__main__':
    validator = EmailValidator()
    samples = [
        "simple@example.com",
        "very.common@example.org",
        "disposable.style.email.with+symbol@example.com",
        "other.email-with-hyphen@example.com",
        "full.name@example.org",
        "user+tag@domain.co.uk",
        "first.last@sub.domain.com",
        "quoted\"name\"@example.com",
        "invalid..double@dot.com",
        "missing@domain",
        "@missinglocal.com",
        "spaces in local@example.com",
        "special!char@domain.com"
    ]
    for email in samples:
        print(f"{email}: {validator.validate(email)}")