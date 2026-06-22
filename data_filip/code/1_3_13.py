import re

_SPECIAL_CHARS = r"[!#$%&'*+\-/=?^_`{|}~]"
ATOM_CHAR = r"[A-Za-z0-9" + SPECIAL_CHARS + "]"
DOT_ATOM_LOCAL = r"(?:" + ATOM_CHAR + r"+\.)*" + ATOM_CHAR + r"+"
QUOTED_PAIR = r"\\[\x00-\x7F]"
QUOTED_LOCAL = r'"(?:' + QUOTED_PAIR + r'|[^"\\])*"'
LOCAL_PART = r"(?:" + DOT_ATOM_LOCAL + r"|" + QUOTED_LOCAL + r")"
DTEXT = r"[\x21-\x5B\x5D-\x7E]"
DOMAIN_LITERAL_CONTENT = r"(?:" + DTEXT + r"|" + QUOTED_PAIR + r")*"
DOMAIN_LITERAL = r"\[" + DOMAIN_LITERAL_CONTENT + r"\]"
DOMAIN_ATOM = r"[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?"
DOMAIN_DOTTED = r"(?:" + DOMAIN_ATOM + r"\.)+" + DOMAIN_ATOM
DOMAIN = r"(?:" + DOMAIN_DOTTED + r"|" + DOMAIN_LITERAL + r")"
FULL_PATTERN = re.compile(r"^" + LOCAL_PART + r"@" + DOMAIN + r"$")

class RFC5322Validator:
    def __init__(self):
        self.pattern = FULL_PATTERN

    def validate(self, address):
        if not isinstance(address, str):
            return False
        return bool(self.pattern.match(address))

    def get_local_part(self, address):
        if not self.validate(address):
            return None
        return address.split('@')[0]

    def get_domain(self, address):
        if not self.validate(address):
            return None
        return address.split('@')[1]

if __name__ == '__main__':
    validator = RFC5322Validator()
    test_cases = [
        "simple@example.com",
        'quoted"local"@example.com',
        'backslash\\quoted"@example.com',
        'invalid..double.dot@example.com',
        'user@[192.168.1.1]',
        "no-at-symbol.com",
        "missing@domain",
        'valid.with-dash+tag@example.org'
    ]
    for case in test_cases:
        is_valid = validator.validate(case)
        local = validator.get_local_part(case)
        domain = validator.get_domain(case)
        print(f"Address: {case} | Valid: {is_valid} | Local: {local} | Domain: {domain}")