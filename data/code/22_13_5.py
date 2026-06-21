import math
import string
import collections

def evaluate_password_entropy(password, threshold=60.0):
    if not isinstance(password, str):
        return {
            'valid': False,
            'entropy': 0.0,
            'length': 0,
            'character_diversity': 0,
            'failures': ['Password must be a string']
        }

    length = len(password)
    
    if length == 0:
        return {
            'valid': False,
            'entropy': 0.0,
            'length': 0,
            'character_diversity': 0,
            'failures': ['Password is empty']
        }

    has_lower = any(c in string.ascii_lowercase for c in password)
    has_upper = any(c in string.ascii_uppercase for c in password)
    has_digit = any(c in string.digits for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    pool_size = 0
    if has_lower:
        pool_size += 26
    if has_upper:
        pool_size += 26
    if has_digit:
        pool_size += 10
    if has_special:
        pool_size += 32
    
    if pool_size == 0:
        return {
            'valid': False,
            'entropy': 0.0,
            'length': length,
            'character_diversity': 0,
            'failures': ['No recognizable character types found']
        }

    entropy = length * math.log2(pool_size)
    
    unique_chars = len(set(password))
    character_diversity = unique_chars / length
    
    failures = []
    
    if entropy < threshold:
        failures.append(f'Entropy {entropy:.2f} bits is below threshold {threshold} bits')
    
    if length < 8:
        failures.append('Password length is less than 8 characters')
        
    if character_diversity < 0.5:
        failures.append('Low character diversity ratio')
        
    if not has_lower:
        failures.append('Missing lowercase letters')
    if not has_upper:
        failures.append('Missing uppercase letters')
    if not has_digit:
        failures.append('Missing digits')
    if not has_special:
        failures.append('Missing special characters')
        
    is_valid = len(failures) == 0
    
    return {
        'valid': is_valid,
        'entropy': round(entropy, 2),
        'length': length,
        'character_diversity': round(character_diversity, 4),
        'failures': failures
    }

if __name__ == '__main__':
    sample_password = "MyP@ssw0rd!"
    result = evaluate_password_entropy(sample_password)
    print(result)