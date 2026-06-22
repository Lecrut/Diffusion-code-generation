import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

MIN_DOMAIN_LENGTH = 2

class EmailVerifier:
    @staticmethod
    def check_local_part(local_part):
        if not local_part:
            return False
        if local_part.startswith('.') or local_part.endswith('.'):
            return False
        if '..' in local_part:
            return False
        return True

    @staticmethod
    def check_domain_part(domain_part):
        parts = domain_part.split('.')
        if len(parts) < 2:
            return False
        for part in parts:
            if not part:
                return False
            if part.startswith('-') or part.endswith('-'):
                return False
            if not part.replace('-', '').isalnum():
                return False
        tld = parts[-1]
        if len(tld) < MIN_DOMAIN_LENGTH:
            return False
        if not tld.isalpha():
            return False
        return True

    @staticmethod
    def validate(email_address):
        if not isinstance(email_address, str):
            return False
        if '@' not in email_address:
            return False
        local, domain = email_address.rsplit('@', 1)
        if not EmailVerifier.check_local_part(local):
            return False
        if not EmailVerifier.check_domain_part(domain):
            return False
        return bool(EMAIL_REGEX.match(email_address))

if __name__ == '__main__':
    verifier_instance = EmailVerifier()
    test_inputs = [
        "john.doe@example.com",
        "invalid.email",
        "user@domain.c",
        ".start@domain.com",
        "end.@domain.com",
        "valid+tag@sub.domain.org",
        "no-at-sign",
        "@missing-local.com",
        "user@-invalid.com",
        "user@inval-id-.com"
    ]
    for sample in test_inputs:
        result = verifier_instance.validate(sample)
        print(result)