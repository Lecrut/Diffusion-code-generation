import re

_LOCAL_ATOM_CHAR = r"[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]"
_LOCAL_ATOM = r"[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+"
_DOT_ATOM_LOCAL = r"(?:" + _LOCAL_ATOM + r"\.)+" + _LOCAL_ATOM

_QUOTED_PAIR = r"\\[\x00-\x7F]"
_QUOTED_STRING = r'"(?:' + _QUOTED_PAIR + r'|[^"\\])*"'

_LOCAL_PART = r"(?:" + _DOT_ATOM_LOCAL + r"|" + _QUOTED_STRING + r")"

_DTEXT = r"[\x21-\x5B\x5D-\x7E]"
_DOMAIN_LITERAL = r"\[(?:" + _DTEXT + r"|" + _QUOTED_PAIR + r")*\]"
_DOMAIN_ATOM = r"[A-Za-z0-9-]+"
_DOMAIN_ATOM_DOT = r"(?:" + _DOMAIN_ATOM + r"\.)+" + _DOMAIN_ATOM

_DOMAIN_PARTS = r"(?:" + _DOMAIN_ATOM_DOT + r"|" + _DOMAIN_LITERAL + r")"

_FULL_PATTERN = r"^" + _LOCAL_PART + r"@" + _DOMAIN_PARTS + r"$"
_EMAIL_REGEX = re.compile(_FULL_PATTERN)

class EmailValidator:
    def __init__(self):
        self._pattern = _EMAIL_REGEX

    def validate(self, address):
        if not isinstance(address, str):
            return False
        return bool(self._pattern.match(address))

    def validate_list(self, addresses):
        results = {}
        for addr in addresses:
            results[addr] = self.validate(addr)
        return results

if __name__ == '__main__':
    validator = EmailValidator()
    test_addresses = [
        "valid.user@domain.com",
        "user+tag@example.org",
        "first.last@sub.domain.co.uk",
        "invalid..double_dot@domain.com",
        "missing_at_sign@domain.com",
        "valid@domain-with-hyphen.com",
        '"quoted@local"@example.com',
        "user@[192.168.1.1]",
        "bad@[invalid_literal]",
        "no_domain@",
        "@no_local.com"
    ]
    results = validator.validate_list(test_addresses)
    for addr, is_valid in results.items():
        print(f"{addr}: {is_valid}")