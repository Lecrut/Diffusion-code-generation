import hashlib
import os
def hash_password(password: str) -> bytes:
    salt = os.urandom(16)
    password_hash = hashlib.pbkdf2_hmac('sha512', password.encode(), salt, 100000)
    return salt + password_hash
if __name__ == '__main__':
    sample_password = "SecurePass123!"
    hashed_data = hash_password(sample_password)
    print(hashed_data.hex())