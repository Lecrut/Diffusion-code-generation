import hashlib
import os

def is_password_compromised(password, compromised_hash_set=None):
    if compromised_hash_set is None:
        compromised_hash_set = _get_compromised_hash_set()
    password_hash = _hash_password(password)
    return password_hash in compromised_hash_set

def _hash_password(password):
    salt = os.urandom(16)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return key.hex()

def _get_compromised_hash_set():
    common_passwords = [
        "password", "123456", "123456789", "qwerty", "abc123",
        "monkey", "1234567", "letmein", "trustno1", "dragon",
        "baseball", "iloveyou", "master", "sunshine", "ashley",
        "football", "shadow", "12345678", "654321", "michael",
        "666666", "superman", "1234567890", "qazwsx", "123123",
        "batman", "access", "111111", "696969", "password1"
    ]
    compromised_hashes = set()
    for pwd in common_passwords:
        h = hashlib.sha256(pwd.encode('utf-8')).hexdigest()
        compromised_hashes.add(h)
    return compromised_hashes

def validate_password_strength(password):
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    return True

def check_password_safety(password):
    if is_password_compromised(password):
        return False
    if not validate_password_strength(password):
        return False
    return True

if __name__ == '__main__':
    test_passwords = [
        "password123",
        "SecureP@ssw0rd!",
        "123456",
        "StrongButNewPass99!",
        "qwertyuiop"
    ]
    for pwd in test_passwords:
        result = check_password_safety(pwd)
        print(f"{pwd}: {result}")