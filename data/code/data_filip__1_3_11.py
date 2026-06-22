import re

def validate_email(email):
    if not isinstance(email, str):
        return False
    if len(email) > 320:
        return False
    pattern = r'^(?:(?:[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+)*)|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}|(?:\d{1,3}\.){3}\d{1,3}|\[(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}|\d+:\d+(?::\d+){7})\])$'
    return re.match(pattern, email) is not None

if __name__ == '__main__':
    test_cases = [
        "simple@example.com",
        "user.name+tag@sub.domain.co.uk",
        "invalid@",
        "@missing.local",
        "user@-example.com",
        "valid@192.168.1.1",
        "quoted\"@example.com",
        "a@b.co",
        "toolong" + "a" * 300 + "@example.com"
    ]
    results = [validate_email(case) for case in test_cases]
    print(results)