import re

_LOCAL_ATOM = r"[A-Za-z0-9!#$%&'*+/=?^_`{|}~\-]"
_LOCAL_ATOM_ONE_OR_MORE = _LOCAL_ATOM + r"+"
_LOCAL_ATOM_DOT_ATOM = r"(?:" + _LOCAL_ATOM_ONE_OR_MORE + r"\.)+" + _LOCAL_ATOM_ONE_OR_MORE
_LOCAL_QUOTED_PAIR = r"\\[\x00-\x7F]"
_LOCAL_QUOTED_STRING = r'"(?:' + _LOCAL_QUOTED_PAIR + r'|[^"\\])*"'
_LOCAL_PART = r"(?:" + _LOCAL_ATOM_DOT_ATOM + r"|" + _LOCAL_QUOTED_STRING + r")"

_DOMAIN_DTEXT = r"[\x21-\x5B\x5D-\x7E]"
_DOMAIN_LITERAL_CONTENT = r"(?:" + _DOMAIN_DTEXT + r"|\\[\x00-\x7F])*"
_DOMAIN_LITERAL = r"\[" + _DOMAIN_LITERAL_CONTENT + r"\]"
_DOMAIN_ATOM = r"[A-Za-z0-9](?:[A-Za-z0-9\-]*[A-Za-z0-9])?"
_DOMAIN_DOT_ATOM = r"(?:" + _DOMAIN_ATOM + r"\.)+" + _DOMAIN_ATOM
_DOMAIN = r"(?:" + _DOMAIN_DOT_ATOM + r"|" + _DOMAIN_LITERAL + r")"

_EMAIL_PATTERN = re.compile(r"^" + _LOCAL_PART + r"@" + _DOMAIN + r"$")

class EmailValidator:
    def __init__(self):
        self._pattern = _EMAIL_PATTERN

    def validate(self, address):
        return bool(self._pattern.match(address))

if __name__ == '__main__':
    validator = EmailValidator()
    test_emails = [
        "user@example.com",
        "user.name@example.co.uk",
        "user+tag@example.org",
        '"quoted"user"@example.com',
        "invalid-email@",
        "another@invalid",
        "user@[192.168.1.1]",
        "test@sub.domain.com"
    ]
    for email in test_emails:
        print(f"{email}: {validator.validate(email)}")