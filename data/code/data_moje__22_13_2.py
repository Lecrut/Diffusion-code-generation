import string
import math
import json

def evaluate_password_entropy(password: str, min_length: int = 8, min_entropy_bits: float = 60.0) -> dict:
    if not isinstance(password, str):
        return {"valid": False, "reasons": ["Password must be a string"]}
    
    reasons = []
    
    if len(password) < min_length:
        reasons.append(f"Password length {len(password)} is less than minimum {min_length}")
    
    entropy_bits = 0.0
    charset_size = 0
    
    if any(c in string.ascii_lowercase for c in password):
        charset_size += 26
    if any(c in string.ascii_uppercase for c in password):
        charset_size += 26
    if any(c in string.digits for c in password):
        charset_size += 10
    if any(c in string.punctuation for c in password):
        charset_size += len(string.punctuation)
        
    if charset_size > 0:
        entropy_bits = len(password) * math.log2(charset_size)
    
    if entropy_bits < min_entropy_bits:
        reasons.append(f"Entropy {entropy_bits:.2f} bits is less than required {min_entropy_bits} bits")
        
    valid = len(reasons) == 0
    
    return {
        "valid": valid,
        "entropy_bits": round(entropy_bits, 2),
        "password_length": len(password),
        "charset_size": charset_size,
        "reasons": reasons
    }

if __name__ == '__main__':
    sample_password = "Str0ng!Pass#99"
    result = evaluate_password_entropy(sample_password)
    print(json.dumps(result, indent=2))
    
    weak_password = "abc"
    weak_result = evaluate_password_entropy(weak_password)
    print(json.dumps(weak_result, indent=2))