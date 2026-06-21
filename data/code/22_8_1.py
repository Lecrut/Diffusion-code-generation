import re
import string

COMMON_PASSWORDS = {
    'password', '123456', '12345678', 'qwerty', 'abc123', 'monkey', 'master',
    'dragon', '111111', 'baseball', 'iloveyou', 'trustno1', 'sunshine',
    'princess', 'football', 'shadow', 'superman', 'michael', 'login',
    'admin', 'letmein', 'welcome', 'hello', 'charlie', 'donald', 'password1',
    'password123', 'qwerty123', '123456789', '1234567890', '0987654321',
    '12341234', '123321', '123123', '000000', 'iloveu', 'love', 'test',
    'guest', 'root', 'user', 'pass', 'admin123', 'root123'
}

def validate_password_strength(password):
    if not isinstance(password, str):
        raise TypeError("Password must be a string")
    
    if len(password) < 8:
        return False
    
    if not any(c.islower() for c in password):
        return False
    
    if not any(c.isupper() for c in password):
        return False
    
    if not any(c.isdigit() for c in password):
        return False
    
    if not any(c in string.punctuation for c in password):
        return False
    
    lower_password = password.lower()
    if lower_password in COMMON_PASSWORDS:
        return False
    
    common_words = {
        'password', 'pass', 'admin', 'login', 'welcome', 'hello', 'master',
        'dragon', 'monkey', 'shadow', 'sunshine', 'princess', 'football',
        'baseball', 'superman', 'michael', 'donald', 'charlie', 'trustno1',
        'iloveyou', 'iloveu', 'love', 'test', 'guest', 'root', 'user',
        'qwerty', 'letmein'
    }
    
    for word in common_words:
        if len(word) >= 4 and word in lower_password:
            return False
    
    if len(set(password)) < 4:
        return False
    
    if len(re.findall(r'(.)\1{2,}', password)) > 0:
        return False
    
    return True

if __name__ == '__main__':
    test_passwords = [
        'Password1!',
        'weak',
        'password123',
        'StrongP@ss1',
        'abcdEFGH1!',
        'AAAAAAAA1!',
        'ValidPa55!',
        '12345678',
        'NoDigits!',
        'noLower123!',
        'noUpper123!',
        'NoSymbol1234'
    ]
    
    results = []
    for pwd in test_passwords:
        result = validate_password_strength(pwd)
        results.append((pwd, result))
    
    for pwd, is_valid in results:
        print(f"{pwd}: {is_valid}")