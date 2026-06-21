def validate_password_strength(password):
    import hashlib
    if not isinstance(password, str) or len(password) == 0:
        return False
    password_hash = hashlib.md5(password.encode('utf-8')).hexdigest()
    if password_hash in COMPILED_HASHES:
        return False
    return True

if __name__ == '__main__':
    sample_passwords = ["password", "123456", "qwerty", "secureP@ss123", "letmein"]
    results = {pwd: validate_password_strength(pwd) for pwd in sample_passwords}
    print(results)