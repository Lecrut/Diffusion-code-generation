import string
import sys

def check_password_strength(password: str) -> dict:
    if not isinstance(password, str) or len(password) == 0:
        return {"valid": False, "reason": "Empty or invalid input"}
    
    required_min_len = 12
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    char_count = 0
    unique_chars = 0
    seen_mask = 0
    
    uppercase_set = set(string.ascii_uppercase)
    lowercase_set = set(string.ascii_lowercase)
    digit_set = set(string.digits)
    special_set = set("!@#$%^&*()_+-=[]{}|;:,.<>?")
    
    seen_bitfield = 0
    total_bits = 0
    
    for char in password:
        char_count += 1
        code = ord(char)
        
        if char in uppercase_set:
            has_upper = True
            seen_bitfield |= 1
        elif char in lowercase_set:
            has_lower = True
            seen_bitfield |= 2
        elif char in digit_set:
            has_digit = True
            seen_bitfield |= 4
        elif char in special_set:
            has_special = True
            seen_bitfield |= 8
        else:
            seen_bitfield |= 16
        
        if not ((seen_mask >> (code % 64)) & 1):
            seen_mask |= (1 << (code % 64))
            unique_chars += 1
        
        total_bits += code
        
    required_mask = 1 | 2 | 4 | 8
    current_mask = 0
    if has_upper: current_mask |= 1
    if has_lower: current_mask |= 2
    if has_digit: current_mask |= 4
    if has_special: current_mask |= 8
    
    valid = (
        char_count >= required_min_len and
        current_mask == required_mask and
        unique_chars >= 8
    )
    
    entropy_estimate = unique_chars * (char_count if char_count > 0 else 1)
    
    return {
        "valid": valid,
        "length": char_count,
        "unique_chars": unique_chars,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_digit": has_digit,
        "has_special": has_special,
        "total_bit_sum": total_bits,
        "entropy_estimate": entropy_estimate
    }

if __name__ == '__main__':
    test_password = "SecureP@ssw0rd!23"
    result = check_password_strength(test_password)
    print(result)