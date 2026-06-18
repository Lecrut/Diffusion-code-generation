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
    def lookup(self, username: str) -> bool:
        return username in self._credentials
if __name__ == '__main__':
    store = CredentialStore()
    sample_passwords = [
        ("alice", hash_password("secret123")),
        ("bob", hash_password("pass456")),
        ("charlie", hash_password("pwd789"))
    ]
    for user, pwd_hash in sample_passwords:
        store.add_user(user, pwd_hash)
    test_users = ["alice", "dave", "eve"]
    results = []
    for u in test_users:
        found = store.lookup(u)
        if found:
            stored_hash = store._credentials[u]
            original_pwd = hash_password("secret123") if u == "alice" else (hash_password("pass456") if u == "bob" else "")
            results.append(f"{u}: {'found' if u in ['alice', 'bob'] and stored_hash == original_pwd else 'not found'}")
    print("\n".join(results))