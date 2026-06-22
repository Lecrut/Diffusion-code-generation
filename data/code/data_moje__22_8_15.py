import re
import unicodedata

def normalize_text(text):
    normalized = unicodedata.normalize('NFKD', text)
    ascii_text = normalized.encode('ASCII', 'ignore').decode('ASCII').lower()
    return re.sub(r'[^a-z0-9]', '', ascii_text)

def get_common_dictionary_words():
    return {
        'password', '123456', '12345678', 'qwerty', 'abc123', 'monkey', 'master',
        'dragon', 'letmein', 'login', 'admin', 'welcome', 'password1', 'iloveyou',
        'starwars', 'superman', 'batman', 'trustno1', 'hello', 'charlie', 'donald',
        'password123', 'qwertyuiop', 'access', 'shadow', 'sunshine', 'princess',
        'football', 'baseball', 'secret', 'love', 'test', 'pass', 'user', 'guest',
        'master', 'admin', 'root', 'system', 'login', 'logout', 'start', 'stop',
        'enable', 'disable', 'create', 'delete', 'update', 'select', 'insert',
        'drop', 'table', 'index', 'view', 'trigger', 'procedure', 'function',
        'package', 'sequence', 'synonym', 'role', 'user', 'privilege', 'grant',
        'revoke', 'audit', 'backup', 'restore', 'encrypt', 'decrypt', 'hash',
        'salt', 'token', 'session', 'cookie', 'header', 'body', 'param', 'query',
        'result', 'error', 'warning', 'info', 'debug', 'trace', 'log', 'event',
        'message', 'signal', 'alarm', 'alert', 'notify', 'email', 'sms', 'push'
    }

def check_password_strength(password):
    common_words = get_common_dictionary_words()
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    
    normalized_password = normalize_text(password)
    if len(normalized_password) < 8:
        return False, "Password contains insufficient alphanumeric characters after normalization."
    
    for word in common_words:
        if word in normalized_password:
            return False, f"Password contains common dictionary word: '{word}'"
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() and not c.isspace() for c in password)
    
    if not (has_upper and has_lower and has_digit and has_special):
        return False, "Password must contain uppercase, lowercase, digit, and special character."
    
    return True, "Password meets NIST guidelines."

if __name__ == '__main__':
    test_passwords = [
        "Weak1",
        "CorrectHorseBatteryStaple",
        "Tr0ub4dor&3",
        "password123!",
        "Str0ng!Pass#2024",
        "qwertyuiop1234"
    ]
    
    for pwd in test_passwords:
        is_valid, message = check_password_strength(pwd)
        print(f"Password: '{pwd}' | Valid: {is_valid} | Message: {message}")