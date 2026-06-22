import re

class EmailValidator:
    _PATTERN = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

    @staticmethod
    def validate(email_address):
        if not isinstance(email_address, str):
            return False
        if not EmailValidator._PATTERN.match(email_address):
            return False
        parts = email_address.split("@")
        if len(parts) != 2:
            return False
        local_part, domain_part = parts
        if not local_part or not domain_part:
            return False
        if local_part.startswith(".") or local_part.endswith("."):
            return False
        if domain_part.startswith(".") or domain_part.endswith("."):
            return False
        if ".." in local_part or ".." in domain_part:
            return False
        return True

if __name__ == "__main__":
    validator_instance = EmailValidator()
    test_values = [
        "alice@example.com",
        "bob.smith+tag@company.co.uk",
        "invalid@.com",
        "missing-tld@",
        "@missing-local.com",
        "spaces in@email.com",
        "valid123@sub.domain.org",
        12345,
        ""
    ]
    for val in test_values:
        print(EmailValidator.validate(val))