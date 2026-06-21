import math
import re

def calculate_password_entropy(password):
    if not password:
        return 0.0
    
    pool_size = 0
    if re.search(r'[a-z]', password):
        pool_size += 26
    if re.search(r'[A-Z]', password):
        pool_size += 26
    if re.search(r'[0-9]', password):
        pool_size += 10
    if re.search(r'[^a-zA-Z0-9]', password):
        pool_size += 33
    
    if pool_size == 0:
        return 0.0
    
    entropy = len(password) * math.log2(pool_size)
    return entropy

def is_password_strong(password):
    entropy = calculate_password_entropy(password)
    return entropy >= 50.0

if __name__ == '__main__':
    test_passwords = ["weak", "Password1", "Str0ng!Passw0rd", "a"]
    results = []
    for pwd in test_passwords:
        strength = is_password_strong(pwd)
        entropy_val = calculate_password_entropy(pwd)
        results.append(f"Password: '{pwd}' -> Is Strong: {strength}, Entropy: {entropy_val:.2f} bits")
    
    for result in results:
        print(result)