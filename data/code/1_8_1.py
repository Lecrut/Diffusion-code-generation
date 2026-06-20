import re
import socket

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    email = email.strip()
    if len(email) > 254:
        return False
    if email.count('@') != 1:
        return False
    local_part, domain_part = email.rsplit('@', 1)
    if len(local_part) > 64:
        return False
    if len(domain_part) > 253:
        return False
    if not local_part or not domain_part:
        return False
    local_pattern = re.compile(r'^(?!\.)[a-zA-Z0-9.!#$%&\'*+/=?^_`{|}~-]+(?<!\.)$')
    if not local_pattern.match(local_part):
        return False
    domain_rules = re.compile(r'^(?!-)[a-zA-Z0-9-]{1,63}(?<!-)(\.(?!-)[a-zA-Z0-9-]{1,63}(?<!-))*\.(?!-)[a-zA-Z]{2,63}(?<!-)$')
    if domain_rules.match(domain_part):
        ip_domain_pattern = re.compile(r'^\[(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\]$')
        if ip_domain_pattern.match(domain_part):
            return True
        try:
            socket.gethostbyname(domain_part)
            return True
        except socket.herror:
            return False
        except Exception:
            return False
    return False

if __name__ == '__main__':
    valid_email = "user@example.com"
    invalid_email = "user@.com"
    result_valid = validate_email(valid_email)
    result_invalid = validate_email(invalid_email)
    print(result_valid)
    print(result_invalid)