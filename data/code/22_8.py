import re

def is_common_word(word: str) -> bool:
    common_passwords = {
        'password', '123456', '12345678', 'qwerty', 'abc123',
        'monkey', '1234567', 'letmein', 'trustno1', 'dragon',
        'baseball', 'iloveyou', 'master', 'sunshine', 'ashley',
        'bailey', 'shadow', 'superman', 'qazwsx', '123123',
        'football', 'mustang', '123456789', 'welcome', 'admin',
        'login', 'passw0rd', 'starwars', 'hello', 'charlie',
        'donald', 'password1', 'password123'
    }
    return word.lower() in common_passwords

def validate_password_strength(password: str) -> bool:
    if len(password) < 8:
        return False
    
    if len(password) > 1024:
        return False
    
    words = re.findall(r'\b\w+\b', password.lower())
    for word in words:
        if len(word) >= 4:
            if is_common_word(word):
                return False
    
    if re.search(r'(.)\1{2,}', password):
        return False
    
    if password.lower() in 'qwertyuiopasdfghjklzxcvbnm':
        return False
    
    if password.lower() in '1234567890' * 2:
        return False
    
    return True

if __name__ == '__main__':
    test_passwords = [
        "SecureP@ssw0rd123",
        "password",
        "123456789",
        "Tr0ub4dor&3",
        "abc123abc123",
        "CorrectHorseBatteryStaple"
    ]
    
    results = []
    for pwd in test_passwords:
        results.append(validate_password_strength(pwd))
    
    print(results)