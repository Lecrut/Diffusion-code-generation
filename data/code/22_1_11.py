import math
import re

def is_strong_password(password: str) -> bool:
    if not isinstance(password, str):
        return False
    
    if len(password) < 8:
        return False
    
    unique_chars = set(password)
    charset_size = 0
    
    if re.search(r'[a-z]', password):
        charset_size += 26
    if re.search(r'[A-Z]', password):
        charset_size += 26
    if re.search(r'[0-9]', password):
        charset_size += 10
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        charset_size += 32
    
    if charset_size == 0:
        return False
    
    entropy = len(password) * math.log2(charset_size)
    
    return entropy >= 60

if __name__ == '__main__':
    result1 = is_strong_password("MyStr0ng!P@ssw0rd")
    print(result1)
    
    result2 = is_strong_password("weak")
    print(result2)
    
    result3 = is_strong_password("abc")
    print(result3)