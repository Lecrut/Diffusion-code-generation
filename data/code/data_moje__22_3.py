import hashlib

COMPROMISED_PASSWORDS_HASHES = {
    "5f4dcc3b5aa765d61d8327deb882cf99",
    "e10adc3949ba59abbe56e057f20f883e",
    "25f9e794323b453885f5181f1b624d0b",
    "81dc9bdb52d04dc20036dbd8313ed055",
    "d033e22ae348aeb5660fc2140aec35850c4da997",
}

def is_password_safe(password: str) -> bool:
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    return hashed_password not in COMPROMISED_PASSWORDS_HASHES

if __name__ == "__main__":
    test_passwords = ["password", "123456", "letmein", "StrongP@ssw0rd!", "qwerty"]
    for pwd in test_passwords:
        result = is_password_safe(pwd)
        print(f"{pwd}: {result}")