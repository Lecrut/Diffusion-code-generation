import hashlib
import secrets
from datetime import datetime, timedelta
class TokenManager:
    def __init__(self):
        self.tokens = {}
        self.secret_key = "super_secret_rotation_2024"
    def generate_token(self) -> str:
        token_data = f"{secrets.token_hex(32)}{datetime.now().isoformat()}"
        hashed_token = hashlib.sha256(f"{self.secret_key}:{token_data}".encode()).hexdigest()
        return hashed_token, datetime.now() + timedelta(hours=1)
    def validate_token(self, token: str) -> bool:
        if not isinstance(token, str):
            raise ValueError("Token must be a string")
        try:
            stored_hash = self.tokens.get(token)
            if stored_hash is None or datetime.now() > stored_hash[1]:
                return False
            expected_hash = hashlib.sha256(f"{self.secret_key}:{token}".encode()).hexdigest()
            if stored_hash[0] != expected_hash:
                return False
            self.tokens[token] = (expected_hash, datetime.now() + timedelta(hours=1))
            return True
        except Exception:
            raise ValueError("Invalid token format or expiration")
if __name__ == '__main__':
    manager = TokenManager()
    generated_token, expiry_time = manager.generate_token()
    print(f"Generated Token (Hashed): {generated_token}")
    print(f"Expiry Time: {expiry_time.isoformat()}")
    is_valid_correct = manager.validate_token(generated_token)
    print(f"Validation of Correct Token: {'Valid' if is_valid_correct else 'Invalid'}")
    invalid_input = "0123456789abcdef"
    is_valid_invalid = manager.validate_token(invalid_input)
    print(f"Validation of Invalid Input: {'Valid' if is_valid_invalid else 'Invalid'}")