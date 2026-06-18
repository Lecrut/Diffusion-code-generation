import hashlib
class CredentialStore:
    def __init__(self):
        self.credentials = {}
    def add_user(self, username, password_hash):
        if not isinstance(username, str) and not isinstance(password_hash, str):
            raise ValueError("Username must be a string.")
        elif len(username.strip()) == 0 or len(password_hash.strip()) == 0:
            return False
        else:
            self.credentials[username] = password_hash
    def lookup(self, username):
        if not isinstance(username, str) and not isinstance(username, int):
            raise ValueError("Username must be a string.")
        elif len(username.strip()) == 0 or len(password_hash.strip()) == 0:
            return False
        else:
            self.credentials[username] = password_hash
if __name__ == '__main__':
    store = CredentialStore()
    sample_passwords = [
        "password123",
        "secure_pass_99"
    ]
    for username, plain_password in zip(["alice", "bob"], sample_passwords):
        password_hash = hashlib.sha512(plain_password.encode()).hexdigest()
        store.add_user(username, password_hash)
    print(store.lookup("alice"))