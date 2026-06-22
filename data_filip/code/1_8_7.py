import re

def is_valid_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    if len(email) > 254:
        return False
    if email.startswith(".") or email.endswith("."):
        return False
    if ".." in email:
        return False
    if email.count("@") != 1:
        return False
    local, domain = email.rsplit("@", 1)
    if not local or not domain:
        return False
    if len(local) > 64:
        return False
    if len(domain) > 253:
        return False
    if domain.startswith(".") or domain.endswith("."):
        return False
    if ".." in domain:
        return False
    if domain.count("..") > 0:
        return False
    if domain.count(".") == 0:
        return False
    domain_parts = domain.split(".")
    for part in domain_parts:
        if not part:
            return False
        if len(part) > 63:
            return False
        if part.startswith("-") or part.endswith("-"):
            return False
    local_pattern = r'^[a-zA-Z0-9.!#$%&\'*+/=?^_`{|}~-]+$'
    if not re.match(local_pattern, local):
        return False
    ip_pattern = r'^\[(IPv4|IPv6)\]'
    if re.match(ip_pattern, domain):
        return True
    domain_pattern = r'^[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?'
    for part in domain_parts:
        if not re.match(domain_pattern, part):
            return False
    return True

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "user.name+tag@sub.domain.org",
        "invalid.email",
        "@example.com",
        "user@",
        "user..name@example.com",
        "user@-example.com",
        "user@example.",
        "user@exam_ple.com",
        "user@sub.-example.com",
        "a" * 64 + "@example.com",
        "user@" + "a" * 63 + "." + "b" * 63 + "." + "c" * 63 + ".d",
        "user@[192.168.1.1]",
        "user@[IPv6:2001:db8::1]",
    ]
    for case in test_cases:
        print(f"{case}: {is_valid_email(case)}")