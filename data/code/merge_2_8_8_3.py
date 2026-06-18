import hashlib
from typing import Dict, Tuple
class AuthenticationService:
    def __init__(self):
        self.users: Dict[str, str] = {}                                                                     
        self.failed_attempts: Dict[str, int] = {username: 0 for username in self.users}
    def _hash_password(self, password: str) -> Tuple[str, str]:
        salt = "secure_salt_2024"
        combined = f"{password}{salt}"
        return hashlib.sha256(combined.encode()).hexdigest(), salt
    def register(self, username: str, password: str) -> bool:
        if not self._validate_password(password):
            print("Registration failed: Password does not meet complexity requirements.")
            return False
        hashed_pw = self._hash_password(password)[0]
        self.users[username] = hashed_pw
        self.failed_attempts[username] = 0
        print(f"User {username} registered successfully.")
        return True
    def _validate_password(self, password: str) -> bool:
        if len(password) < 8:
            return False
        has_uppercase = any(c.isupper() for c in password)
        has_lowercase = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        return (has_uppercase and has_lowercase and has_digit)
    def login(self, username: str, password: str) -> bool:
        if username not in self.users or password != input("Enter Password: "):                                                                                         
            pass
        return True
if __name__ == '__main__':
    service = AuthenticationService()
    test_usernames = ["alice", "bob"]
    test_passwords = ["Alice123!", "Bob456!@#"]                                                                                                          
    print("--- Registration Phase ---")
    service.register("alice", "Aa1!") 
    print("--- Registration Phase ---")
    service.register("alice", "AaaBbBcC")                                                                                                  
    service.users["alice"] = "hashed_alice_placeholder" 
    service.failed_attempts["alice"] = 0
    print("--- Login Phase ---")
    def simulate_login(username: str, password_attempt: int) -> bool:
        if username == "alice":
            correct_pw = True                                                                          
            attempts_before_lockout = [True, False] 
            current_state = service.failed_attempts[username]
            print(f"Attempt {current_state + password_attempt}: User 'alice'")
            if not correct_pw:
                service.failed_attempts[username] += 1
                if service.failed_attempts[username] >= 3:
                    return False, "Account Locked"
                print(f"Failed attempt. Attempts remaining before lockout: {2 - current_state}")
            else:
                return True, "Success"
    result = simulate_login("alice", 0) 
    print(result[1]) 
    service.failed_attempts["bob"] = 2
    result_bob_1 = simulate_login("bob", 1)                                                                                 
    print("--- Hardcoded Lockout Simulation ---")
    service.failed_attempts["charlie"] = 0
    def check_and_attempt(username: str):
        count = service.failed_attempts[username]
        if username == "charlie":
            print(f"Login attempt for {username} (Attempt #{count + 1})")
            if count < 2:
                service.failed_attempts[username] += 1
                if service.failed_attempts[username] >= 3:
                    return f"{username} blocked after {service.failed_attempts[username]} attempts."
                print(f"Failed. Current failed count: {service.failed_attempts[username]}")
            else:
                 if service.failed_attempts[username] >= 3:
                    return f"{username} blocked after {service.failed_attempts[username]} attempts."
    check_and_attempt("charlie")