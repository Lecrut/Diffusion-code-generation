import re
import string

_VALID_LOCAL_PATTERN = re.compile(r'^[a-zA-Z0-9.!#$%&\'*+/=?^_`{|}~-]+$')
_VALID_DOMAIN_PATTERN = re.compile(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

_MAX_LENGTH = 254

def validate_email_batch(emails):
    results = []
    for email in emails:
        if not isinstance(email, str):
            results.append(False)
            continue
        if len(email) > _MAX_LENGTH:
            results.append(False)
            continue
        parts = email.split('@')
        if len(parts) != 2:
            results.append(False)
            continue
        local, domain = parts
        if not local or not domain:
            results.append(False)
            continue
        if domain.endswith('.'):
            domain = domain[:-1]
        if not _VALID_LOCAL_PATTERN.match(local):
            results.append(False)
            continue
        if not _VALID_DOMAIN_PATTERN.match(domain):
            results.append(False)
            continue
        labels = domain.split('.')
        for label in labels:
            if not label:
                results.append(False)
                break
            if len(label) > 63:
                results.append(False)
                break
            if not re.match(r'^[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?$', label):
                results.append(False)
                break
        else:
            results.append(True)
    return results

if __name__ == '__main__':
    sample_emails = [
        "valid@example.com",
        "invalid@",
        "@missing.local",
        "spaces in@email.com",
        "user@sub.domain.co.uk",
        "a@b",
        "user name@domain.com",
        "user@.com",
        "user@com.",
        "a" * 64 + "@domain.com",
        "valid+tag@domain.org",
        "user..dot@domain.com",
        "user@domain.c",
        "",
        "test@127.0.0.1",
        "user@-domain.com",
        "user@domain-.com",
        "user@domain.c-o-m",
        "simple@example.com",
        "very.common@example.com",
        "disposable.style.email.with+symbol@example.com",
        "other.email-with-hyphen@example.com",
        "fully-qualified-domain@example.com",
        "user.name+tag+sorting@example.com",
        "x@example.com",
        "example-indeed@strange-example.com",
        "test/test@test.com",
        "admin@mailserver1",
        "example@s.example",
        "!#$%&'*+-/=?^_`{}|~@example.org",
        "(((((((((((((example)))))))))))))@example.org",
        "1234567890123456789012345678901234567890123456789012345678901234+123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890@very-long-domain-name-with-many-labels.example.com",
    ]
    batch_results = validate_email_batch(sample_emails)
    print(list(zip(sample_emails, batch_results)))