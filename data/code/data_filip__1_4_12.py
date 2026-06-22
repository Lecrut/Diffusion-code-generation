import re

class EmailSyntaxChecker:
    _PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[a-zA-Z]{2,}$")

    @staticmethod
    def check(address):
        if not isinstance(address, str):
            return False
        parts = address.split("@")
        if len(parts) != 2:
            return False
        local, domain = parts
        if not local or not domain:
            return False
        if ".." in local:
            return False
        if domain.startswith(".") or domain.endswith("."):
            return False
        if not EmailSyntaxChecker._PATTERN.match(address):
            return False
        return True

if __name__ == "__main__":
    checker = EmailSyntaxChecker()
    samples = [
        "valid.user@domain.com",
        "invalid@.com",
        "@missing.com",
        "no-at-sign.com",
        "user@domain.co.uk",
        "123@456.net"
    ]
    for s in samples:
        print(checker.check(s))