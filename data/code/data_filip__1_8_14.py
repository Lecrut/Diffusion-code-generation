import re

def validate_email(email):
    if not isinstance(email, str):
        return False
    if not email or not 1 <= len(email) <= 254:
        return False
    at_count = email.count('@')
    if at_count != 1:
        return False
    local_part, domain_part = email.rsplit('@', 1)
    if not local_part or not domain_part:
        return False
    if len(local_part) > 64:
        return False
    if len(domain_part) > 253:
        return False
    local_pattern = r"^((?!.*\.\.)[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\\\"\\]|[^\"\\]+)*\")$"
    if not re.match(local_pattern, local_part):
        return False
    domain_pattern = r"^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$"
    if not re.match(domain_pattern, domain_part):
        return False
    return True

if __name__ == '__main__':
    samples = [
        "user@example.com",
        "invalid.email@",
        "@missing.local",
        "user.name+tag@example.co.uk",
        "invalid..double@example.com",
        "",
        "spaces in@name.com",
        "user@.invalid.com",
        "user@domain",
        "a@b.co",
        "very.long.local.part.that.exceeds.sixty.four.characters.limit@domain.com",
        "user@[192.168.1.1]",
        "test@example.museum"
    ]
    for s in samples:
        print(validate_email(s))