import re

_EMAIL_PATTERN = re.compile(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')

def check_email_format(email_address):
    return bool(_EMAIL_PATTERN.match(email_address))

class EmailValidator:
    def __init__(self, pattern_string):
        self.pattern = re.compile(pattern_string)

    def validate(self, text):
        return bool(self.pattern.match(text))

    def batch_check(self, items):
        return {item: self.validate(item) for item in items}

if __name__ == '__main__':
    test_cases = [
        "alpha.beta@server.org",
        "bad-format@domain",
        "test.user+tag@sub.domain.co",
        "@invalid.com",
        "no_at_sign.com",
        "valid_name123@example-site.net"
    ]

    validator_instance = EmailValidator(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')
    print(validator_instance.batch_check(test_cases))