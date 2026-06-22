import re
import string

_DOMAIN_PATTERN = re.compile(
    r'^(?=.{1,253}\.[a-z0-9]|\.[a-z0-9]{1,63})([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,63}$'
)

_VALID_LOCAL_CHARACTERS = set(string.ascii_letters + string.digits + '._%+-')

def is_valid_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    
    if email.count('@') != 1:
        return False
    
    local_part, domain_part = email.split('@')
    
    if not local_part:
        return False
    
    if len(local_part) > 64:
        return False
    
    for char in local_part:
        if char not in _VALID_LOCAL_CHARACTERS:
            return False
    
    if local_part[0] == '.' or local_part[-1] == '.':
        return False
    
    if '..' in local_part:
        return False
    
    if not _DOMAIN_PATTERN.match(domain_part):
        return False
    
    return True

if __name__ == '__main__':
    sample_email = 'user.name+tag@subdomain.example.com'
    result = is_valid_email(sample_email)
    print(result)