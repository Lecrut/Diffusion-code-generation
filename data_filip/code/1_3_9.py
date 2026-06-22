import re
_SPECIAL_CHARS = r"[!#$%&'*+/=?^_`{|}~]"
ATOM_CHAR = r"[A-Za-z0-9" + SPECIAL_CHARS + r"-]"
LOCAL_ATOM = r"(?:" + ATOM_CHAR + r"(?:\." + ATOM_CHAR + r")*|" + ATOM_CHAR + r"+)"
QUOTED_PAIR = r"\\[\x00-\x7F]"
QUOTED_LOCAL = r'"(?:' + QUOTED_PAIR + r'|[^"\\])*"'
LOCAL_PART = r"(?:" + LOCAL_ATOM + r"|" + QUOTED_LOCAL + r")"
DTEXT = r"[\x21-\x5B\x5D-\x7E]"
DOMAIN_LITERAL_CONTENT = r"(?:" + DTEXT + r"|" + QUOTED_PAIR + r")*"
DOMAIN_LITERAL = r"\[" + DOMAIN_LITERAL_CONTENT + r"\]"
DOMAIN_ATOM = r"[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?"
DOMAIN_ATOM_PARTS = r"(?:" + DOMAIN_ATOM + r"\.)+" + DOMAIN_ATOM
DOMAIN = r"(?:" + DOMAIN_ATOM_PARTS + r"|" + DOMAIN_LITERAL + r")"
PATTERN_STR = r"^" + LOCAL_PART + r"@" + DOMAIN + r"$"
EMAIL_REGEX = re.compile(PATTERN_STR)

class EmailValidator:
    def __init__(self):
        self._regex = EMAIL_REGEX
    
    def is_valid(self, address):
        if not isinstance(address, str):
            return False
        return bool(self._regex.fullmatch(address))
    
    def get_details(self, address):
        if self.is_valid(address):
            return {"valid": True, "address": address}
        return {"valid": False, "address": address, "reason": "Invalid format"}

def validate_email_rfc5322(email):
    validator = EmailValidator()
    return validator.is_valid(email)

if __name__ == '__main__':
    samples = [
        "user@example.com",
        "user+tag@sub.domain.co.uk",
        "user.name@domain.org",
        "user@domain",
        "invalid@",
        "@domain.com",
        '"quoted"@domain.com',
        "user@[192.168.1.1]",
        "user@-invalid.com",
        "user@domain..com"
    ]
    
    validator_instance = EmailValidator()
    
    for s in samples:
        result = validator_instance.get_details(s)
        print(f"{s}: {result['valid']}")
    
    print(f"Simple check for user@example.com: {validate_email_rfc5322('user@example.com')}")