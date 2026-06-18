import hashlib
from typing import Optional
class SecureAuthService:
    def __init__(self):
        self.authorized_keys = {
            "user_001": hashlib.sha256(b"session_token_alpha").hexdigest(),
            "admin_007": hashlib.sha256(b"secure_admin_beta").hexdigest()
        }
    def verify_key(self, provided_key: str) -> Optional[str]:
        if not isinstance(provided_key, str):
            return None
        key_hash = hashlib.sha256(provided_key.encode()).hexdigest()
        for user_id, expected_hash in self.authorized_keys.items():
            if key_hash == expected_hash:
                return user_id
        return None
if __name__ == '__main__':
    service = SecureAuthService()
    test_cases = [
        "user_001",
        "admin_007", 
        "invalid_user"
    ]
    for key in test_cases:
        result = service.verify_key(key)
        if result is not None:
            print(f"Key '{key}' verified successfully. User ID: {result}")
        else:
            print(f"Key '{key}' rejected.")