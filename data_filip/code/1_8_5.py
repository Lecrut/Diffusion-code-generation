import re
import string

def is_valid_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    
    if len(email) > 254:
        return False
    
    if "@" not in email:
        return False
    
    local_part, _, domain_part = email.rpartition("@")
    
    if not local_part or not domain_part:
        return False
    
    if len(local_part) > 64:
        return False
    
    domain_labels = domain_part.split(".")
    
    if len(domain_labels) < 2:
        return False
    
    for label in domain_labels:
        if not label:
            return False
        if len(label) > 63:
            return False
        if label.startswith("-") or label.endswith("-"):
            return False
    
    if ".." in domain_part:
        return False
    
    invalid_chars = set(string.punctuation.replace("-", "").replace(".", "").replace("_", ""))
    invalid_chars.update({" ", "\t", "\n", "\r"})
    
    if any(c in invalid_chars for c in local_part):
        return False
    
    if any(c in invalid_chars for c in domain_part):
        return False
    
    if local_part.startswith(".") or local_part.endswith("."):
        return False
    
    if local_part.startswith('"') and local_part.endswith('"'):
        inner = local_part[1:-1]
        if "\\\\" in inner:
            return False
    else:
        if local_part.startswith('"') or local_part.endswith('"'):
            return False
    
    pattern = re.compile(r'^[a-zA-Z0-9](?:[a-zA-Z0-9_.+-]*[a-zA-Z0-9])?$')
    if not pattern.match(local_part):
        return False
    
    domain_pattern = re.compile(r'^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$')
    if not domain_pattern.match(domain_part):
        return False
    
    if domain_part.startswith("-") or domain_part.endswith("-"):
        return False
    
    return True

if __name__ == "__main__":
    print(is_valid_email("user@example.com"))
    print(is_valid_email("invalid-email@.com"))
    print(is_valid_email("@missinglocal.com"))
    print(is_valid_email("no@at"))
    print(is_valid_email("double@@at.com"))
    print(is_valid_email("user.name+tag@sub.domain.com"))
    print(is_valid_email("user..name@example.com"))
    print(is_valid_email("user@-invalid.com"))
    print(is_valid_email("user@invalid-.com"))
    print(is_valid_email(""))
    print(is_valid_email(None))
    print(is_valid_email("user@127.0.0.1"))