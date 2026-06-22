import math
import re

def calculate_password_strength(password: str) -> bool:
    if not password:
        return False
    
    char_set_size = 0
    
    if re.search(r'[a-z]', password):
        char_set_size += 26
    if re.search(r'[A-Z]', password):
        char_set_size += 26
    if re.search(r'\d', password):
        char_set_size += 10
    if re.search(r'[^a-zA-Z0-9]', password):
        char_set_size += 33
    
    if char_set_size == 0:
        return False
    
    length = len(password)
    entropy = length * math.log2(char_set_size)
    
    return entropy >= 50.0

if __name__ == '__main__':
    sample_weak = "abc123"
    sample_strong = "Tr0ub4dor&3#Complex"
    
    result_weak = calculate_password_strength(sample_weak)
    result_strong = calculate_password_strength(sample_strong)
    
    print(result_weak)
    print(result_strong)