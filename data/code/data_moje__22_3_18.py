import hashlib
import secrets
from typing import List

COMMON_COMPROMISED_HASHES = {
    "5f4dcc3b5aa765d61d8327deb882cf99",
    "e10adc3949ba59abbe56e057f20f883e",
    "25d947080d39c092388b5c9295112902",
    "202cb962ac59075b964b07152d234b70",
    "098f6bcd4621d373cade4e832627b4f6"
}

def validate_password_strength(password: str, min_length: int = 12) -> bool:
    if len(password) < min_length:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(not char.isalnum() for char in password):
        return False
    return True

def is_password_compromised(password: str) -> bool:
    password_hash = hashlib.md5(password.encode('utf-8')).hexdigest()
    return password_hash in COMMON_COMPROMISED_HASHES

def check_password_security(password: str) -> dict:
    is_valid_strength = validate_password_strength(password)
    is_compromised = is_password_compromised(password)
    
    if not is_valid_strength:
        return {
            "valid": False,
            "reason": "Password does not meet complexity requirements"
        }
    
    if is_compromised:
        return {
            "valid": False,
            "reason": "Password is in the list of compromised passwords"
        }
    
    return {
        "valid": True,
        "reason": "Password passed all security checks"
    }

if __name__ == '__main__':
    test_password_1 = "Str0ng!P@ssw0rd2024"
    test_password_2 = "password123"
    test_password_3 = "Short1!"
    
    result_1 = check_password_security(test_password_1)
    result_2 = check_password_security(test_password_2)
    result_3 = check_password_security(test_password_3)
    
    print(result_1)
    print(result_2)
    print(result_3)