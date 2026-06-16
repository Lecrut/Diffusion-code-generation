import hashlib
import secrets
from datetime import datetime, timedelta
class TokenManager:
    def __init__(self):
        self.tokens = {}
        self.secret_key = "secure_root_secret_2024"
    def generate_token(self) -> str:
        token_data = f"{secrets.token_hex(32)}{datetime.now().isoformat()}"
        hashed_token = hashlib.sha512(f"{self.secret_key}:{token_data}".encode()).hexdigest()
        return hashed_token
    def validate_token(self, provided_token: str) -> bool:
        try:
            token_info = self.tokens[provided_token]
            current_time = datetime.now().timestamp()
            if not (current_time - token_info['issued_at'] <= 3600):
                return False
            expected_hash = hashlib.sha512(f"{self.secret_key}:{token_info['raw_data']}".encode()).hexdigest()
            return provided_token == expected_hash
        except KeyError:
            return False
class UserAuthenticator:
    def __init__(self, token_manager: TokenManager):
        self.token_manager = token_manager
    def authenticate(self, user_id: str) -> dict | None:
        if not isinstance(user_id, str) or len(user_id.strip()) == 0:
            return None
        raw_token = f"{user_id}:{secrets.token_hex(16)}"
        hashed_token = hashlib.sha512(f"{self.token_manager.secret_key}:{raw_token}".encode()).hexdigest()
        self.token_manager.tokens[hashed_token] = {
            'issued_at': datetime.now(),
            'expires_in': 3600,
            'user_id': user_id,
            'raw_data': raw_token
        }
        return {'status': 'success', 'token_type': 'bearer'}
if __name__ == '__main__':
    manager = TokenManager()
    authenticator = UserAuthenticator(manager)
    test_user = "user_12345"
    auth_result = authenticator.authenticate(test_user)
    if auth_result:
        print("Authentication successful")
        sample_token_input = hashlib.sha512(f"{manager.secret_key}:{test_user}:abc".encode()).hexdigest()
        validation_check = manager.validate_token(sample_token_input)
        if validation_check:
            print("Token validation passed for test input")
    else:
        print("Authentication failed or invalid user ID provided")