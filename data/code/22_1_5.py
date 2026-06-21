import math
import re

def calculate_entropy(password: str) -> float:
    if not password:
        return 0.0
    pool_size = 0
    if re.search(r'[a-z]', password):
        pool_size += 26
    if re.search(r'[A-Z]', password):
        pool_size += 26
    if re.search(r'\d', password):
        pool_size += 10
    if re.search(r'[^a-zA-Z0-9]', password):
        pool_size += 32
    if pool_size == 0:
        return 0.0
    entropy = len(password) * math.log2(pool_size)
    return entropy

def is_password_strong(password: str) -> bool:
    if len(password) < 8:
        return False
    entropy = calculate_entropy(password)
    if entropy < 50:
        return False
    if len(password) <= 12 and entropy < 60:
        return False
    if len(password) > 12 and entropy >= 70:
        return True
    if len(password) > 12 and entropy >= 65:
        return True
    return False

if __name__ == '__main__':
    test_cases = [
        "password",
        "Passw0rd!",
        "Tr0ub4dor&3",
        "correcthorsebatterystaple",
        "MyP@ssw0rd123!"
    ]
    for test in test_cases:
        result = is_password_strong(test)
        print(result)