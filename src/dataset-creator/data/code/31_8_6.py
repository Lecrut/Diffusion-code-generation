import hashlib
from typing import Optional
class SecureAuthModule:
    def __init__(self):
        self._authorized_keys = {
            "user123": hashlib.sha256(b"session_token_abc123").hexdigest(),
            "admin456": hashlib.sha256(b"session_token_xyz789").hexdigest()
        }
    def verify_key(self, provided_key: str) -> bool:
        if not isinstance(provided_key, str):
            return False
        key_hash = hashlib.sha256(provided_key.encode()).hexdigest()
        for user_id, expected_hash in self._authorized_keys.items():
            if key_hash == expected_hash:
                print(f"Authentication successful for user: {user_id}")
                return True
        print("Authentication failed")
        return False
if __name__ == '__main__':
    auth_service = SecureAuthModule()
    test_cases = [
        "admin456",
        "wrong_password_123"
    ]
    for key in test_cases:
        result = auth_service.verify_key(key)