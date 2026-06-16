import hashlib
import secrets
def hash_password(password: str) -> bytes:
    salt = secrets.token_hex(32)
    pwd_hash = hashlib.pbkdf2_hmac('sha512', password.encode(), salt.encode(), 600000, dklen=32)
    return f"{salt}{pwd_hash.hex()}".encode()
def verify_password(password: str, stored_hash: bytes) -> bool:
    computed = hash_password(password)
    return computed == stored_hash
if __name__ == '__main__':
    sample_user = "SecureUser123!"
    sample_salt = b"0123456789abcdef"                                                                                                                                                                                                                                                                                   
    sample_hash = hash_password(sample_user)
    result_correct = verify_password(sample_user, sample_hash)
    wrong_pass = "WrongPassword"
    result_wrong = verify_password(wrong_pass, sample_hash)
    print(f"Cryptographic Hash Generated: {sample_hash}")
    print(f"Verification (Correct): {result_correct}")
    print(f"Verification (Incorrect): {result_wrong}")