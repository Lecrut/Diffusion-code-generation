import hashlib
from typing import Optional
class SecureAuthModule:
    def __init__(self):
        self.authorized_keys = {
            "user_001": hashlib.sha256(b"session_token_alpha").hexdigest(),
            "admin_007": hashlib.sha256(b"master_session_beta").hexdigest()
        }
    def verify_key(self, provided_key: str) -> bool:
        return provided_key in self.authorized_keys
if __name__ == '__main__':
    auth_service = SecureAuthModule()
    test_cases = [
        "user_001",
        "admin_007",
        "invalid_user"
    ]
    for user_id in test_cases:
        is_valid = auth_service.verify_key(user_id)
        print(f"{user_id}: {'Authorized' if is_valid else 'Unauthorized'}")