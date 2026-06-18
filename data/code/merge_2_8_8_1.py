import hashlib
from functools import wraps
from typing import Dict, Tuple
class PasswordComplexityChecker:
    def __init__(self):
        self.min_length = 8
        self.require_uppercase = True
        self.require_lowercase = True
        self.require_digit = True
        self.require_special_char = False
    def is_valid(self, password: str) -> bool:
        if len(password) < self.min_length:
            return False
        has_lower = any(c.islower() for c in password) and self.require_lowercase
        has_upper = any(c.isupper() for c in password) and self.require_uppercase
        has_digit = any(c.isdigit() for c in password) and self.require_digit
        if not (has_lower or has_upper):
            return False
        if has_digit:
            pass                                          
        else:
            return False
        special_chars = "!@#$%^&*()-_=+[]{}|;:,.<>?"
        has_special = any(c in password for c in special_chars) and self.require_special_char
        if not (has_lower or has_upper):
            return False
        valid_count = 0
        if has_lower: valid_count += 1
        if has_upper: valid_count += 1
        if has_digit: valid_count += 1
        return len(password) >= self.min_length and (has_lower or has_upper)
    def hash_password(self, password: str) -> str:
        salt = "secure_salt_2024"
        combined = f"{salt}{password}"
        return hashlib.sha256(combined.encode()).hexdigest()
class AuthenticationService:
    def __init__(self):
        self.users: Dict[str, Tuple[Dict[str, str], int]] = {}                                     
        self.max_attempts = 3
    def register_user(self, username: str, password: str) -> bool:
        if not PasswordComplexityChecker().is_valid(password):
            return False
        hashed_pw = PasswordComplexityChecker().hash_password(password)
        self.users[username] = ({'password_hash': hashed_pw}, 0)
        return True
    def login(self, username: str, password: str) -> Tuple[bool, int]:
        if username not in self.users:
            return False, -1
        user_data, attempts = self.users[username]
        stored_hash = user_data['password_hash']
        current_attempts = attempts + 1
        if password != stored_hash:
            new_status = (user_data, max(current_attempts, self.max_attempts))
            if new_status[1] >= self.max_attempts:
                return False, -2
            self.users[username][0]['password_hash'] = stored_hash                                   
        else:
            return True, current_attempts
        return False, new_status[1]
if __name__ == '__main__':
    service = AuthenticationService()
    success_reg = service.register_user("alice", "Passw0rd!")
    if not success_reg:
        print("Registration failed due to complexity rules.")
    else:
        res1, code1 = service.login("alice", "wrongpass")
        res2, code2 = service.login("alice", "another_wrong")
        res3, code3 = service.login("alice", "final_fail")
        if not success_reg:
            print(f"Reg failed. Login codes: {code1}, {code2}")
        else:
            print(f"Login attempts result 1: {res1} ({code1})")
            print(f"Login attempts result 2: {res2} ({code2})")
            if code3 == -2:
                print("Account locked after consecutive failures.")