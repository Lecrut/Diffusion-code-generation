import hashlib
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()
class CredentialStore:
    def __init__(self):
        self._credentials = {}                        
    def add_user(self, username: str, password_hash: str) -> None:
        if not isinstance(username, str) or len(username.strip()) == 0:
            raise ValueError("Invalid username")
        if not isinstance(password_hash, str):
            raise TypeError("Password hash must be a string")
        self._credentials[username] = password_hash
    def lookup(self, username: str) -> bool | None:
        return self._credentials.get(username.strip())
if __name__ == '__main__':
    store = CredentialStore()
    sample_passwords = [
        ("alice", hash_password("secret1")),
        ("bob", hash_password("password2")),
        ("charlie", hash_password("pass345"))
    ]
    for user, pwd_hash in sample_passwords:
        store.add_user(user, pwd_hash)
    test_cases = [
        "alice",
        "dave",
        ""
    ]
    print(f"{'Username':<10} | {'Status'}")
    print("-" * 35)
    for user in test_cases:
        result = store.lookup(user) if isinstance(user, str) else None
        status = "Found" if result is not None else "Not Found"
        print(f"{user:<10} | {status}")