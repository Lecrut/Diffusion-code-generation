import re

_MAX_LENGTH = 254
_LOCAL_PATTERN = re.compile(r'^[a-zA-Z0-9._%+-]+$')
_DOMAIN_PATTERN = re.compile(r'^[a-zA-Z0-9.-]+$')
_TLD_PATTERN = re.compile(r'^[a-zA-Z]{2,}$')

def validate_email(email):
    if not isinstance(email, str):
        return False
    if len(email) == 0 or len(email) > _MAX_LENGTH:
        return False
    at_index = email.find('@')
    if at_index == -1 or at_index == len(email) - 1:
        return False
    if email.count('@') != 1:
        return False
    local_part = email[:at_index]
    domain_part = email[at_index+1:]
    if len(local_part) == 0:
        return False
    if not _LOCAL_PATTERN.match(local_part):
        return False
    if len(domain_part) == 0:
        return False
    if not _DOMAIN_PATTERN.match(domain_part):
        return False
    if domain_part.startswith('-') or domain_part.endswith('-'):
        return False
    if '..' in domain_part:
        return False
    last_dot_index = domain_part.rfind('.')
    if last_dot_index == -1:
        return False
    tld = domain_part[last_dot_index+1:]
    if not _TLD_PATTERN.match(tld):
        return False
    return True

if __name__ == '__main__':
    samples = [
        "user@example.com",
        "invalid.email@",
        "another@invalid",
        "name.with.dots+tag@sub.domain.co",
        "spaces in@email.com",
        "@missinglocal.com",
        "valid123@sub.domain.org",
        "",
        "a@b.c",
        "test@domain..com",
        123,
        "user@domain-.com",
        "user-.domain.com"
    ]
    for s in samples:
        print(validate_email(s))