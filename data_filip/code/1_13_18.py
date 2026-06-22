import re
import time

def validate_emails(emails):
    pattern = re.compile(
        r'^(?P<user>[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+)*)'
        r'@'
        r'(?P<domain>[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*)$'
    )
    results = []
    for email in emails:
        if not isinstance(email, str):
            results.append(False)
            continue
        if len(email) > 320:
            results.append(False)
            continue
        match = pattern.match(email)
        if match:
            user_part = match.group('user')
            domain_part = match.group('domain')
            if not user_part or not domain_part:
                results.append(False)
                continue
            if domain_part.startswith('.') or domain_part.endswith('.') or '..' in domain_part:
                results.append(False)
                continue
            if user_part.startswith('.') or user_part.endswith('.') or '..' in user_part:
                results.append(False)
                continue
            results.append(True)
        else:
            results.append(False)
    return results

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "user.name@sub.domain.co.uk",
        "user+tag@example.com",
        "invalid.email@",
        "@example.com",
        "user@.com",
        "user@example.",
        "user@exam_ple.com",
        "user@-example.com",
        "user@example.com.",
        "user..name@example.com",
        "user@example..com",
        "user@example_cook.com",
        "user@exam-ple.com",
        "user_name@exam-ple.co.uk",
        "user_name@example.com",
        "user@192.168.1.1",
        "user@[192.168.1.1]",
        "a@b.co",
        "ab@c.d",
        ""
    ]
    validation_results = validate_emails(sample_emails)
    print(validation_results)