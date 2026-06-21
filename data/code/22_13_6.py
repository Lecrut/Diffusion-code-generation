import math
import string
import re

def evaluate_password_entropy(password: str) -> dict:
    if not password:
        return {"valid": False, "reasons": ["Password is empty"]}

    reasons = []
    length = len(password)
    
    if length < 8:
        reasons.append("Password length is less than 8 characters")

    lowercase_count = sum(1 for c in password if c in string.ascii_lowercase)
    uppercase_count = sum(1 for c in password if c in string.ascii_uppercase)
    digit_count = sum(1 for c in password if c in string.digits)
    symbol_count = sum(1 for c in password if c in string.punctuation)

    if lowercase_count == 0:
        reasons.append("No lowercase letters")
    if uppercase_count == 0:
        reasons.append("No uppercase letters")
    if digit_count == 0:
        reasons.append("No digits")
    if symbol_count == 0:
        reasons.append("No special symbols")

    if length >= 12 and len(reasons) == 0:
        charset_size = 0
        if lowercase_count > 0:
            charset_size += 26
        if uppercase_count > 0:
            charset_size += 26
        if digit_count > 0:
            charset_size += 10
        if symbol_count > 0:
            charset_size += 32
        
        entropy = length * math.log2(charset_size) if charset_size > 0 else 0
        
        if entropy >= 60:
            return {"valid": True, "reasons": [], "entropy": entropy}
        else:
            reasons.append(f"Entropy {entropy:.2f} bits is below threshold")

    elif length >= 8 and len(reasons) == 0:
        charset_size = 0
        if lowercase_count > 0:
            charset_size += 26
        if uppercase_count > 0:
            charset_size += 26
        if digit_count > 0:
            charset_size += 10
        if symbol_count > 0:
            charset_size += 32
        
        entropy = length * math.log2(charset_size) if charset_size > 0 else 0
        
        if entropy >= 50:
            return {"valid": True, "reasons": [], "entropy": entropy}
        else:
            reasons.append(f"Entropy {entropy:.2f} bits is below threshold")

    if not reasons:
        reasons.append("Password does not meet complexity requirements")
    
    return {"valid": False, "reasons": reasons}

if __name__ == '__main__':
    result = evaluate_password_entropy("Str0ng!Pass#2023")
    print(result)