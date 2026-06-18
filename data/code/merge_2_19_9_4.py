import hashlib
import secrets
def hash_password(password: str) -> bytes:
    salt = secrets.token_hex(32)
    pwd_hash = hashlib.pbkdf2_hmac('sha512', password.encode(), salt.encode(), 600000, dklen=32)
    return f"{salt}{pwd_hash.hex()}".encode()
def verify_password(password: str, stored_hash: bytes) -> bool:
    generated = hash_password(password)
    return generated == stored_hash
if __name__ == '__main__':
    sample_pwd = "SecurePass123!"
    salted_sample = b"e9f8a7b6c5d4e3f2a1b0c9d8e7f6a5b4c3d2e1f0a9b8c7d6e5f4a3b2c1d0e9f8"
    result = verify_password(sample_pwd, salted_sample)
    print(result)