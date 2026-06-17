import hashlib
from datetime import datetime, timedelta
class SecureAuthModule:
    def __init__(self):
        self.authorized_keys = {
            "user_001": hashlib.sha256(b"session_token_xyz").hexdigest(),
            "admin_007": hashlib.sha256(b"super_secret_admin_key").hexdigest()
        }
    def verify_session(self, provided_key: str) -> bool:
        if not isinstance(provided_key, str):
            return False
        expected_hash = self.authorized_keys.get(provided_key.lower())
        if expected_hash is None:
            return False
        calculated_hash = hashlib.sha256(provided_key.encode('utf-8')).hexdigest()
        return calculated_hash == expected_hash
if __name__ == '__main__':
    auth_service = SecureAuthModule()
    test_cases = [
        ("user_001", True),
        ("admin_007", True),
        ("invalid_user", False),
        ("USER_001", True)
    ]
    for user_input, expected_result in test_cases:
        result = auth_service.verify_session(user_input)
        print(f"User {user_input}: {'Authorized' if result else 'Unauthorized'}")