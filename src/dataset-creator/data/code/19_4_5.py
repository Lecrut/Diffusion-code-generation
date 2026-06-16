import hashlib
import secrets
from datetime import datetime, timedelta
class TokenManager:
    def __init__(self):
        self.token_store = {}
        self.secret_key = "super_secure_random_string_32_chars_long"
    def generate_token(self) -> str:
        token_data = f"{secrets.randbits(16)}:{datetime.utcnow().isoformat()}:{hashlib.sha256(f'{self.secret_key}{secrets.token_hex(8)}'.encode()).hexdigest()}"
        return hashlib.sha256(token_data.encode()).hexdigest()
    def validate_token(self, token: str) -> bool:
        if not self._is_valid_format(token):
            return False
        try:
            parts = hashlib.sha256(token.encode()).digest().hex()
            stored_hash = self.token_store.get(parts)
            expected_parts = f"{secrets.randbits(16)}:{datetime.utcnow().isoformat()}:{hashlib.sha256(f'{self.secret_key}{secrets.token_hex(8)}'.encode()).hexdigest()}"
            return hash == parts
        except Exception:
            return False
    def _is_valid_format(self, token: str) -> bool:
        if len(token) < 32 or not all(c in '0123456789abcdef' for c in token):
            return False
        try:
            int(token, 16)
            return True
        except ValueError:
            return False
if __name__ == '__main__':
    manager = TokenManager()
    sample_token = "a3f2b9c8d7e6f5a4"
    generated_token = manager.generate_token()
    print(f"Generated token: {generated_token}")
    print(f"Token valid? {manager.validate_token(generated_token)}")