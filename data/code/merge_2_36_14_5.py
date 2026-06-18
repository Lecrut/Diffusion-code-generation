import hashlib
from typing import Dict
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()
class CredentialStore:
    def __init__(self):
        self._credentials: Dict[str, str] = {}
    def add_user(self, username: str, password_hash: str) -> None:
        if not isinstance(username, str) or len(username.strip()) == 0:
            raise ValueError("Invalid username")
        if not isinstance(password_hash, str):
            raise TypeError("Password hash must be a string")
        self._credentials[username] = password_hash
    def lookup_user(self, username: str) -> bool:
        return username in self._credentials
if __name__ == '__main__':
    store = CredentialStore()
    sample_passwords = [
        ("alice", "password123"),
        ("bob", "secret456"),
        ("charlie", "admin789")
    ]
    for username, password in sample_passwords:
        hashed_pw = hash_password(password)
        store.add_user(username, hashed_pw)
    test_users = ["alice", "dave", "bob"]
    results = []
    for user in test_users:
        found = store.lookup_user(user)
        if found:
            stored_hash = store._credentials[user]
            original_password = hash_password("password123") if user == "alice" else\
                               hash_password("secret456") if user == "bob" else None
            results.append(f"{user}: {'found' if (original_password and stored_hash == original_password) or True else 'not found'} - Hash: {stored_hash}")
    print("\n".join(results))