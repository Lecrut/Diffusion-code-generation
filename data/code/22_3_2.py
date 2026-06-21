def is_password_compromised(password: str) -> bool:
    compromised_hashes = {
        "5f4dcc3b5aa765d61d8327deb882cf99",
        "e10adc3949ba59abbe56e057f20f883e",
        "25f9e794323b453885f5181f1b624d0b",
        "d8578edf8458ce06fbc5bb76a58c5ca4",
        "6b86b273ff34fce19d6b804eff5a3f57"
    }
    import hashlib
    input_hash = hashlib.md5(password.encode('utf-8')).hexdigest()
    return input_hash in compromised_hashes

if __name__ == '__main__':
    sample_passwords = ["password", "123456", "admin", "securePass123", "qwerty"]
    results = []
    for pwd in sample_passwords:
        is_compromised = is_password_compromised(pwd)
        results.append((pwd, is_compromised))
    for pwd, status in results:
        print(f"{pwd}: {status}")