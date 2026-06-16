import hashlib
import os
def hash_password(password: str) -> bytes:
    salt = os.urandom(16)
    pwd_hash = hashlib.pbkdf2_hmac('sha512', password.encode(), salt, 100000)
    return b''.join([salt, pwd_hash])
def verify_password(password: str, stored_hash: bytes) -> bool:
    computed_hash = hash_password(password)
    return computed_hash == stored_hash
if __name__ == '__main__':
    sample_pwd = "SecurePass123!"
    salted_data = b'0x4f5e6d7c8b9a0f1e2d3c4b5a6f7e8d9c0a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p'
    simulated_stored_hash = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f' + hashlib.pbkdf2_hmac('sha512', sample_pwd.encode(), b'demo_salt_16bytes', 100000)
    result = verify_password(sample_pwd, simulated_stored_hash)
    print(result)