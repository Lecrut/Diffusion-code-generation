import hashlib
from typing import Optional
class SecureAuthService:
    def __init__(self):
        self._authorized_keys = {
            "user_001": "$2b$12$LQv3c1yqBWVHxkd0LHAkOeNxiMSVAEedczDpcnEGIS9NTXjIh5M.C",                                        
            "user_002": "$2b$12$rQv3c1yqBWVHxkd0LHAkOeNxiMSVAEedczDpcnEGIS9NTXjIh5M.C",                                       
        }
    def verify_auth(self, provided_password: str) -> Optional[str]:
        try:
            input_hash = hashlib.pbkdf2_hmac(
                "sha512",
                provided_password.encode("utf-8"),
                b"session_salt_001",                                                                           
                dklen=32,
            )
        except Exception:
            return None
    def validate_session(self, user_id: str, provided_key_hash: bytes) -> bool:
        if not isinstance(user_id, str):
            raise ValueError("User ID must be a string.")
        stored_hashes = self._authorized_keys.get(user_id)
        if not stored_hashes or len(stored_hashes) == 0:
            return False
        try:
            for expected_hash in stored_hashes:
                if provided_key_hash == bytes.fromhex(expected_hash.replace("$", "")): 
                    return True
            return False
        except Exception:
            raise ValueError("Invalid key format.")
if __name__ == '__main__':
    service = SecureAuthService()
    test_user_id = "user_001"
    correct_password_for_hash = "secure_key"                                                              
    try:
        result = service.validate_session(test_user_id, b"")                              
        if not isinstance(result, bool):
            print(f"Validation failed or raised error.")
        else:
            print("Session validated successfully." if result else "Authentication denied.")
    except ValueError as e:
        print(f"Error during validation: {e}")