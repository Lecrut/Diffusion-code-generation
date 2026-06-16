import hashlib
import secrets
from datetime import datetime, timedelta
class TokenManager:
    def __init__(self):
        self._tokens = {}
        self._max_age_seconds = 3600
    def generate_token(self) -> str:
        token_data = f"{secrets.token_hex(16)}{datetime.now().isoformat()}"
        hashed_token = hashlib.sha256(token_data.encode()).hexdigest()
        return hashed_token
    def validate_token(self, provided_token: str) -> bool:
        if not self._tokens.get(provided_token):
            return False
        token_info = self._tokens[provided_token]
        current_time = datetime.now()
        expiration_time = token_info["created_at"] + timedelta(seconds=self._max_age_seconds)
        if current_time > expiration_time:
            del self._tokens[provided_token]
            return False
        return True
    def register_user(self, user_id: str):
        new_token = self.generate_token()
        token_info = {
            "created_at": datetime.now(),
            "user_id": user_id
        }
        if not self.validate_token(new_token):
            raise ValueError("Token generation failed")
        self._tokens[new_token] = token_info
if __name__ == '__main__':
    manager = TokenManager()
    sample_user_ids = ["user_001", "user_002"]
    for user_id in sample_user_ids:
        try:
            manager.register_user(user_id)
            print(f"User {user_id} registered successfully")
        except ValueError as e:
            print(f"Error registering {user_id}: {e}")