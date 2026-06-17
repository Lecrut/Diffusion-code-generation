import hashlib
from typing import Dict
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()
class CredentialStore:
    def __init__(self):
        self._users: Dict[str, str] = {}
    def add_user(self, username: str, password: str) -> None:
        hashed_pw = hash_password(password)
        if not (1 <= len(username) <= 256):
            raise ValueError("Username must be between 1 and 256 characters.")
        self._users[username] = hashed_pw
    def lookup_user(self, username: str) -> bool:
        return username in self._users
if __name__ == '__main__':
    store = CredentialStore()
    store.add_user("alice", "secret123")
    store.add_user("bob", "password456")
    print(store.lookup_user("alice"))        
    print(store.lookup_user("charlie"))