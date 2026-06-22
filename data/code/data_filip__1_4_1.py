import re

class EmailValidator:
    _LOCAL_PART_PATTERN = r'[a-zA-Z0-9._%+-]+'
    _DOMAIN_PART_PATTERN = r'[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*'
    _TLD_PATTERN = r'\.[a-zA-Z]{2,}'
    _FULL_PATTERN = re.compile(
        rf'^{_LOCAL_PART_PATTERN}@{_DOMAIN_PART_PATTERN}{_TLD_PATTERN}$'
    )

    @staticmethod
    def validate(address):
        if not isinstance(address, str):
            return False
        return bool(EmailValidator._FULL_PATTERN.match(address))

if __name__ == '__main__':
    validator = EmailValidator()
    test_cases = [
        "alex.morgan@tech-corp.io",
        "support_team@server.dev",
        "user@invalid",
        "@nodomain.com",
        "missing.tld@",
        "double@@at.com",
        "simple@domain.org"
    ]
    
    results = [
        (email, validator.validate(email))
        for email in test_cases
    ]
    
    for email, is_valid in results:
        print(f"{email}: {is_valid}")