import re
import re

_LOCAL_ATOM_CHARS = r"[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]"
_LOCAL_ATOM_NON_EMPTY = _LOCAL_ATOM_CHARS + r"+"
_LOCAL_ATOM_WITH_DOTS = r"(?:" + _LOCAL_ATOM_NON_EMPTY + r"\.)*" + _LOCAL_ATOM_NON_EMPTY
_QUOTED_PAIR = r"\\[\x00-\x7F]"
_LOCAL_QUOTED_STR = r'"(?:' + _QUOTED_PAIR + r'|[^"\\])*"'
_LOCAL_PART = r"(?:" + _LOCAL_ATOM_WITH_DOTS + r"|" + _LOCAL_QUOTED_STR + r")"

_DOMAIN_DTEXT = r"[\x21-\x5B\x5D-\x7E]"
_DOMAIN_PAIR = r"\\[\x00-\x7F]"
_DOMAIN_LITERAL_CONTENT = r"(?:" + _DOMAIN_DTEXT + r"|" + _DOMAIN_PAIR + r")*"
_DOMAIN_LITERAL = r"\[" + _DOMAIN_LITERAL_CONTENT + r"\]"
_DOMAIN_ATOM = r"[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?"
_DOMAIN_ATOM_WITH_DOTS = r"(?:" + _DOMAIN_ATOM + r"\.)*" + _DOMAIN_ATOM
_DOMAIN_PART = r"(?:" + _DOMAIN_ATOM_WITH_DOTS + r"|" + _DOMAIN_LITERAL + r")"
_FULL_RFC5322_RE = re.compile(r"^" + _LOCAL_PART + r"@" + _DOMAIN_PART + r"$")

class EmailValidator:
    def __init__(self):
        self._regex = _FULL_RFC5322_RE

    def check_format(self, address):
        if not isinstance(address, str):
            return False
        return bool(self._regex.match(address))

    def get_pattern_source(self):
        return self._regex.pattern

if __name__ == '__main__':
    validator = EmailValidator()
    test_addresses = [
        "user.name+tag@example.co.uk",
        "simple@example",
        "quoted@domain[192.168.0.1]",
        "bad..double@domain.com",
        "no_at_sign.com",
        "valid_local@valid-domain.net",
        "user@invalid-",
        "\"quoted\\string\"@example.com"
    ]
    for addr in test_addresses:
        result = validator.check_format(addr)
        print(addr + ": " + str(result))