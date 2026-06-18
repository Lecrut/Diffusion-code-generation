import hashlib
from typing import Dict, Tuple
class AuthenticationService:
    def __init__(self):
        self.users: Dict[str, dict] = {}
        self.consecutive_failures: Dict[str, int] = {}
    def _hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()
    def register_user(self, username: str, password: str):
        if not (len(password) >= 8 and 
                any(c.isdigit() for c in password) and 
                any(c.isalpha() for c in password)):
            raise ValueError("Password must be at least 8 characters long and contain letters and numbers.")
        self.users[username] = {
            'password_hash': self._hash_password(password),
            'consecutive_failures': 0
        }
    def _check_complexity(self, password: str) -> bool:
        return (len(password) >= 8 and 
                any(c.isdigit() for c in password) and 
                any(c.isalpha() for c in password))
    def login_attempt(self, username: str, password: str) -> Tuple[bool, str]:
        if username not in self.users or not self._check_complexity(password):
            return False, "Invalid credentials or complex password required."
        stored_hash = self.users[username]['password_hash']
        current_failures = self.consecutive_failures.get(username, 0)
        if password != stored_hash:
            new_failure_count = min(current_failures + 1, 5)
            self.consecutive_failures[username] = new_failure_count
            if new_failure_count >= 3:
                return False, "Too many failed attempts. Account locked."
            return False, "Invalid credentials or complex password required."
        del self.users[username]['password_hash']
        del self.consecutive_failures[username]
        return True, "Login successful"
if __name__ == '__main__':
    service = AuthenticationService()
    try:
        service.register_user("alice", "Pass123!")
    except ValueError as e:
        print(f"Registration failed: {e}")
    test_cases = [
        ("alice", "wrongpass"),                                  
        ("alice", "WrongCase!@#"),                                           
    ]
    results = []
    for user in ["bob"]:
        service.register_user(user, "BobUser1!")
    for username, pwd in test_cases:
        success, msg = service.login_attempt(username, pwd)
        results.append((username, success, msg))
        if not success and 'locked' in msg.lower():
            break
    print("Login Results:")
    for user, success, message in results:
        status = "SUCCESS" if success else f"{message}"
        print(f"[{user}] {status}")