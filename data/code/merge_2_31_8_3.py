import hashlib
from typing import Optional
class SecureAuthModule:
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
    auth_service = SecureAuthModule()
    test_cases = [
        "user_001",
        "admin_007", 
        "invalid_user_xyz"
    ]
    for key in test_cases:
        result = auth_service.verify_key(key)
        print(f"Key: {key} -> Status: {'Authorized' if result else 'Rejected'}")