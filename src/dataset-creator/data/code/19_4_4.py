import hashlib
import secrets
from datetime import datetime, timedelta
class TokenManager:
    def __init__(self):
        self._tokens = {}
        self._max_age_seconds = 3600
    def generate_token(self) -> str:
        token_data = f"{secrets.token_hex(16)}:{datetime.utcnow().isoformat()}"
        hashed_token = hashlib.sha256(token_data.encode()).hexdigest()
        return hashed_token, datetime.now() + timedelta(seconds=self._max_age_seconds)
    def validate_token(self, provided_hash: str) -> bool:
        current_time = datetime.utcnow()
        for stored_hash in self._tokens.keys():
            if provided_hash == stored_hash and (current_time - self._tokens[stored_hash]).total_seconds() < 0:
                return True
        return False
    def revoke_token(self, token_hash: str):
        del self._tokens[token_hash]
if __name__ == '__main__':
    manager = TokenManager()
    valid_hash, expiry_time = manager.generate_token()
    print(f"Generated Token Hash: {valid_hash}")
    print("Token Expiry:", expiry_time)
    test_input = "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6"
    is_valid = manager.validate_token(test_input)
    print("Is Test Input Valid?", is_valid)