import math
import string

def calculate_password_entropy(password):
    if not password:
        return 0.0
    
    charset_size = 0
    has_lowercase = any(c in string.ascii_lowercase for c in password)
    has_uppercase = any(c in string.ascii_uppercase for c in password)
    has_digits = any(c in string.digits for c in password)
    has_special = any(c in string.punctuation or not c.isalnum() for c in password)
    
    if has_lowercase:
        charset_size += 26
    if has_uppercase:
        charset_size += 26
    if has_digits:
        charset_size += 10
    if has_special:
        charset_size += 32
    
    if charset_size == 0:
        return 0.0
    
    length = len(password)
    entropy = length * math.log2(charset_size)
    
    return entropy

def is_password_strong(password, min_entropy=60.0):
    if not isinstance(password, str):
        return False
    
    if len(password) < 8:
        return False
    
    entropy = calculate_password_entropy(password)
    
    if entropy < min_entropy:
        return False
    
    if any(char == ' ' for char in password):
        return False
    
    if len(set(password)) < 3:
        return False
    
    return True

if __name__ == '__main__':
    sample_passwords = [
        "Weak1!",
        "StrongP@ssw0rd!23",
        "12345678",
        "abcdefgh",
        "Tr0ub4dor&3",
        "P@$$w0rd!XyZ99",
        "short1!",
        "Aa1!Aa1!Aa1!Aa1!",
        "Hello World 1!",
        "aaaaaaab1!"
    ]
    
    results = []
    for pwd in sample_passwords:
        result = is_password_strong(pwd)
        results.append(result)
    
    print(results)