import re

class EmailValidator:
    @staticmethod
    def validate(email: str) -> bool:
        if not isinstance(email, str):
            return False
        pattern = re.compile(
            r"^(?P<local>[a-zA-Z0-9_.+-]+)@"
            r"(?P<domain>[a-zA-Z0-9-]+)"
            r"(\.(?P=tld>[a-zA-Z0-9-]+))+$"
        )
        if not pattern.match(email):
            return False
        local, domain = email.split('@')
        if local.startswith('.') or local.endswith('.'):
            return False
        if '..' in local:
            return False
        if domain.startswith('.') or domain.endswith('.'):
            return False
        if domain.startswith('-') or domain.endswith('-'):
            return False
        if domain.count('.') < 1:
            return False
        return True

if __name__ == '__main__':
    test_emails = [
        "user.name+tag@example.co.uk",
        "invalid-email@",
        "another@invalid",
        "correct@sub.domain.org"
    ]
    for email in test_emails:
        result = EmailValidator.validate(email)
        print(f"{email}: {result}")