import re

_ATTEXT = r"[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]"
_DOT_ATOM_LOCAL = r"(?:" + _ATTEXT + r"+\.)*" + _ATTEXT + r"+"
_QUOTED_PAIR = r"\\[\x00-\x7F]"
_QUOTED_STRING = r'"(?:' + _QUOTED_PAIR + r'|[^"\\])*"'
_LOCAL_PART = r"(?:" + _DOT_ATOM_LOCAL + r"|" + _QUOTED_STRING + r")"

_DTEXT = r"[!-Z[-~]"
_DOMAIN_LITERAL_CONTENT = r"(?:" + _DTEXT + r"|" + _QUOTED_PAIR + r")*"
_DOMAIN_LITERAL = r"\[" + _DOMAIN_LITERAL_CONTENT + r"\]"

_DOMAIN_NAME = r"(?:" + _DOT_ATOM_LOCAL + r")"
_DOMAIN_PART = r"(?:" + _DOMAIN_NAME + r"|" + _DOMAIN_LITERAL + r")"

_PATTERN_STRING = r"^" + _LOCAL_PART + r"@" + _DOMAIN_PART + r"$"
_COMPILED_PATTERN = re.compile(_PATTERN_STRING)

def validate_email_rfc5322(email_address):
    if not isinstance(email_address, str):
        return False
    return bool(_COMPILED_PATTERN.match(email_address))

class EmailValidationService:
    def __init__(self):
        self._validator = validate_email_rfc5322

    def check(self, address):
        return self._validator(address)

    def batch_check(self, addresses):
        return {addr: self._validator(addr) for addr in addresses}

if __name__ == '__main__':
    service = EmailValidationService()
    test_inputs = [
        "simple@example.com",
        "user+tag@sub.domain.org",
        '"quoted"@example.com',
        "invalid@",
        "@invalid.com",
        "no@domain",
        "bad..double@dot.com",
        "test@[192.168.1.1]",
        "normal.user@valid-domain.net"
    ]
    for item in test_inputs:
        result = service.check(item)
        print(result)