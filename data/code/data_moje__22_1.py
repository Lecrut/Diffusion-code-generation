import math
import string
import re

def calculate_entropy(password: str) -> float:
    if not password:
        return 0.0
    pool_size = 0
    if re.search(r'[a-z]', password):
        pool_size += 26
    if re.search(r'[A-Z]', password):
        pool_size += 26
    if re.search(r'[0-9]', password):
        pool_size += 10
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        pool_size += 33
    if not pool_size:
        return 0.0
    entropy = len(password) * math.log2(pool_size)
    return entropy

def is_password_strong(password: str) -> bool:
    entropy = calculate_entropy(password)
    return entropy >= 60

if __name__ == '__main__':
    sample_passwords = [
        "weak",
        "BetterPass1",
        "Tr0ub4dor&3",
        "correcthorsebatterystaple"
    ]
    for pwd in sample_passwords:
        print(is_password_strong(pwd))