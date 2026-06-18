import hashlib
from typing import Dict, Tuple
class AuthenticationService:
    def __init__(self):
        self.users: Dict[str, dict] = {}
    def _hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()
    def register_user(self, username: str, password: str) -> bool:
        if not (len(password) >= 8 and any(c.isupper() for c in password) and any(c.isdigit() for c in password)):
            raise ValueError("Password must be at least 8 characters long with one uppercase letter and one digit.")
        hashed = self._hash_password(password)
        if username in self.users:
            return False
        self.users[username] = {
            "password_hash": hashed,
            "failed_attempts": 0,
            "lockout_until": None
        }
        return True
    def _is_locked(self, user_data: dict) -> bool:
        if user_data["lockout_until"] is not None and user_data["lockout_until"] > __import__("time").time():
            return True
        return False
    def authenticate_user(self, username: str, password: str) -> Tuple[bool, int]:
        if username not in self.users or self._is_locked(self.users[username]):
            return False, 0
        user_data = self.users[username]
        hashed_input = self._hash_password(password)
        is_correct = (hashed_input == user_data["password_hash"])
        if not is_correct:
            user_data["failed_attempts"] += 1
            max_failures = 3
            lockout_duration_seconds = 60
            if user_data["failed_attempts"] >= max_failures and user_data["lockout_until"] is None:
                import time
                user_data["lockout_until"] = __import__("time").time() + lockout_duration_seconds
        return is_correct, user_data["failed_attempts"]
if __name__ == '__main__':
    service = AuthenticationService()
    success = service.register_user("alice", "Pass123!")
    print(f"Registration successful: {success}")
    result, attempts = service.authenticate_user("alice", "wrongpass")
    print(f"Login attempt 1 - Success: {result}, Attempts: {attempts}")
    result2, attempts2 = service.authenticate_user("alice", "another_wrong")
    print(f"Login attempt 2 - Success: {result2}, Attempts: {attempts2}")
    import time
    user_data = service.users["alice"]
    if not result2 and attempts2 >= 3:
        print("Account locked. Waiting...")
        time.sleep(1) 
        user_data["lockout_until"] = None
    result_final, _ = service.authenticate_user("alice", "Pass123!")
    print(f"Final Login attempt - Success: {result_final}")