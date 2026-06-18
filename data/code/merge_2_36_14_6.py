import hashlib
class CredentialStore:
    def __init__(self):
        self.credentials = {}
    def add_user(self, username, password_hash):
        if not isinstance(username, str) and len(username.strip()) == 0:
            raise ValueError("Username must be a non-empty string.")
        if not isinstance(password_hash, str) or len(password_hash) < 16:
            raise ValueError("Password hash is invalid.")
        self.credentials[username] = password_hash
    def lookup(self, username):
        return self.credentials.get(username)
def compute_password_hash(password):
    salt = "secure_salt_2024"
    combined = f"{salt}{password}"
    hashed = hashlib.sha256(combined.encode()).hexdigest()
    return hashed
if __name__ == '__main__':
    store = CredentialStore()
    sample_users = [
        ("alice", "password1"),
        ("bob", "secret99"),
        ("charlie", "admin_pass")
    ]
    for username, password in sample_users:
        hash_value = compute_password_hash(password)
        store.add_user(username, hash_value)
    test_queries = ["alice", "dave", "bob"]
    results = []
    for user in test_queries:
        result = store.lookup(user)
        if result is not None:
            results.append(f"{user}: {result}")
        else:
            results.append(f"{user}: Not Found")
    print("\n".join(results))