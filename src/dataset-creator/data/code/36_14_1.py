import hashlib
from typing import Dict, List
class SecureCredentialLookup:
    def __init__(self):
        self.credentials: Dict[str, str] = {}
    def hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()
    def add_user(self, username: str, password: str) -> None:
        hashed_pwd = self.hash_password(password)
        if not self.credentials.get(username):
            self.credentials[username] = hashed_pwd
    def lookup_user(self, username: str) -> bool:
        return username in self.credentials
if __name__ == '__main__':
    system = SecureCredentialLookup()
    sample_users = [
        ("alice", "password123"),
        ("bob", "secret456"),
        ("charlie", "admin789")
    ]
    for user, pwd in sample_users:
        system.add_user(user, pwd)
    test_lookup = ["alice", "dave"]
    print("User Lookup Results:")
    for u in test_lookup:
        result = system.lookup_user(u)
        if result:
            stored_hash = system.credentials[u]
            print(f"{u}: Found (Hash: {stored_hash[:16]}...)")
        else:
            print(f"{u}: Not found")