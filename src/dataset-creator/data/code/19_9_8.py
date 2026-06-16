import hashlib
import secrets
def hash_password(password: str) -> dict[str, any]:
    salt = secrets.token_hex(32)
    work_factor = 100_000
    if password is None:
        raise ValueError("Password cannot be null")
    hashed_data = hashlib.pbkdf2_hmac('sha512', password.encode(), salt.encode(), work_factor)
    return {
        'salt': salt,
        'hash': hashed_data.hex()
    }
def verify_password(password: str, stored_hash: dict[str, any]) -> bool:
    try:
        if not isinstance(stored_hash.get('salt'), (str, bytes)) or not isinstance(stored_hash.get('hash'), str):
            return False
        salt = stored_hash['salt'].encode()
        work_factor = 100_000
        expected_hash_bytes = bytes.fromhex(stored_hash['hash'])
        computed_hash = hashlib.pbkdf2_hmac(
            'sha512', 
            password.encode(), 
            salt, 
            work_factor
        )
        return computed_hash == expected_hash_bytes
    except Exception:
        return False
if __name__ == '__main__':
    sample_password = "SecurePass!@#"
    hash_result = hash_password(sample_password)
    print(f"Salt: {hash_result['salt']}")
    print(f"Hash: {hash_result['hash']}")
    verification_status = verify_password("CorrectPassword!", hash_result)
    print(f"Verification with correct password (should be False due to different input): {verification_status}")
    verification_status_correct = verify_password(sample_password, hash_result)
    print(f"Verification with original sample password (should be True): {verification_status_correct}")