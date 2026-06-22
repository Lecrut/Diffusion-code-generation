import re

_LOCAL_UNQUOTED_CHAR = r"[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]"
_DOT_ATOM_LOCAL = r"(?:" + _LOCAL_UNQUOTED_CHAR + r"(?:\.?" + _LOCAL_UNQUOTED_CHAR + r")*)"
_QUOTED_PAIR = r"\\[\x00-\x7F]"
_QUOTED_LOCAL = r'"(?:' + _QUOTED_PAIR + r'|[^"\\])*"'
_LOCAL_PART_PATTERN = r"(?:" + _DOT_ATOM_LOCAL + r"|" + _QUOTED_LOCAL + r")"

_DOMAIN_ATOM_CHAR = r"[A-Za-z0-9]"
_DOMAIN_ATOM_START = r"(?:" + _DOMAIN_ATOM_CHAR + r"(?:[A-Za-z0-9-]*" + _DOMAIN_ATOM_CHAR + r")?)"
_DOMAIN_ATOM_CHAIN = r"(?:\." + _DOMAIN_ATOM_START + r")+"
_DOMAIN_LITERAL_DTEXT = r"[\x21-\x5B\x5D-\x7E]"
_DOMAIN_LITERAL_PAIR = r"\\[\x00-\x7F]"
_DOMAIN_LITERAL_BODY = r"(?:" + _DOMAIN_LITERAL_DTEXT + r"|" + _DOMAIN_LITERAL_PAIR + r")*"
_DOMAIN_LITERAL = r"\[" + _DOMAIN_LITERAL_BODY + r"\]"
_DOMAIN_PATTERN = r"(?:" + _DOMAIN_ATOM_CHAIN + r"|" + _DOMAIN_LITERAL + r")"

_RFC5322_REGEX = re.compile(r"^" + _LOCAL_PART_PATTERN + r"@" + _DOMAIN_PATTERN + r"$")

def is_valid_email_address(address):
    return bool(_RFC5322_REGEX.match(address))

class EmailValidator:
    def __init__(self):
        self.pattern = _RFC5322_REGEX

    def check(self, address):
        return self.pattern.match(address) is not None

if __name__ == '__main__':
    test_addresses = [
        "user.name+tag@domain.co.uk",
        '"quoted local"@example.com',
        "simple@example.com",
        "invalid..double.dot@example.com",
        "missing@domain",
        "@example.com",
        "user@[192.168.1.1]",
        "user@bad domain.com"
    ]
    
    validator = EmailValidator()
    for addr in test_addresses:
        result = validator.check(addr)
        print(f"{addr}: {result}")
    
    standalone_result = is_valid_email_address("another.valid@sub.domain.org")
    print(standalone_result)