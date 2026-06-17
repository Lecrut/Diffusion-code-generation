import hashlib
from functools import wraps
from typing import Tuple
class SecureAuthService:
    def _hash_key(self, key: str) -> str:
        return hashlib.sha256(key.encode('utf-8')).hexdigest()
    def verify_session(self, provided_key: str, authorized_keys: list[str]) -> bool:
        if not isinstance(provided_key, str):
            raise TypeError("Key must be a string")
        if len(authorized_keys) == 0:
            return False
        stored_hash = self._hash_key(authorized_keys[0])
        user_input_hash = self._hash_key(provided_key)
        return stored_hash == user_input_hash
    def generate_session_token(self, key: str) -> Tuple[str, int]:
        token_data = f"{key}:{self.generate_nonce()}"
        token = hashlib.sha256(token_data.encode('utf-8')).hexdigest()[:16]
        ttl_seconds = 300
        return token, ttl_seconds
    def _generate_nonce(self) -> str:
        import secrets
        nonce_length = 32
        return secrets.token_hex(nonce_length)
if __name__ == '__main__':
    service = SecureAuthService()
    authorized_keys_sample = ["admin_123", "user_xyz"]
    test_cases = [
        ("correct_key_hashed", True),
        ("wrong_key_input", False),
        ("empty_string", False)
    ]
    for input_val, expected_result in test_cases:
        result = service.verify_session(input_val, authorized_keys_sample)
        print(f"Input: {input_val}, Expected: {expected_result}, Got: {result}")