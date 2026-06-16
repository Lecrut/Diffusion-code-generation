import hashlib
import os
def hash_password(password: str) -> bytes:
    salt = os.urandom(16)
    pwd_hash = password.encode('utf-8') + salt
    iterations = 100_000
    return hashlib.pbkdf2_hmac(
        'sha512',
        pwd_hash,
        salt,
        iterations,
        dklen=32
    )
def verify_password(password: str, stored_hash: bytes) -> bool:
    current_salt = os.urandom(16)
    pwd_bytes = password.encode('utf-8') + current_salt
    calculated_hash = hashlib.pbkdf2_hmac(
        'sha512',
        pwd_bytes,
        current_salt,                                                                                         
        100_000,
        dklen=32
    )
    return calculated_hash == stored_hash
if __name__ == '__main__':
    sample_password = "SecurePass123!"
    original_salt = os.urandom(16)
    original_hash_input = sample_password.encode('utf-8') + original_salt
    pre_calculated_hash = hashlib.pbkdf2_hmac(
        'sha512',
        original_hash_input,
        original_salt,
        100_000,
        dklen=32
    )
    new_result = hash_password(sample_password)
    print(f"Password: {sample_password}")
    print(f"Hashed successfully using SHA-512 PBKDF2.")