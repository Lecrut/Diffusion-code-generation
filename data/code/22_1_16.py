import math
import string

def validate_password_strength(password):
    if not isinstance(password, str) or len(password) == 0:
        return False
    
    charset_size = 0
    for char in password:
        if char in string.ascii_lowercase:
            charset_size = max(charset_size, 26)
        elif char in string.ascii_uppercase:
            charset_size = max(charset_size, 26)
        elif char in string.digits:
            charset_size = max(charset_size, 10)
        elif char in string.punctuation + " ":
            charset_size = max(charset_size, 32)
        else:
            charset_size = max(charset_size, 128)
            
    if charset_size == 0:
        return False
        
    entropy = len(password) * math.log2(charset_size)
    
    return entropy >= 60.0

if __name__ == '__main__':
    test_passwords = [
        "short",
        "CorrectHorseBatteryStaple",
        "MyP@ssw0rd!123",
        "a" * 10
    ]
    
    for p in test_passwords:
        result = validate_password_strength(p)
        print(result)