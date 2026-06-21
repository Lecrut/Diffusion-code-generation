import hashlib
import struct

def check_password_strength(password: str) -> dict:
    if not password:
        return {"score": 0, "criteria_met": False}
    
    length = len(password)
    bits = [bit for bit in password.encode('utf-8')]
    
    upper_mask = 0x00
    lower_mask = 0x00
    digit_mask = 0x00
    special_mask = 0x00
    
    for byte_val in bits:
        if 65 <= byte_val <= 90:
            upper_mask |= 1
        elif 97 <= byte_val <= 122:
            lower_mask |= 1
        elif 48 <= byte_val <= 57:
            digit_mask |= 1
        elif (33 <= byte_val <= 47) or (58 <= byte_val <= 64) or (91 <= byte_val <= 96) or (123 <= byte_val <= 126):
            special_mask |= 1
            
    has_upper = bool(upper_mask)
    has_lower = bool(lower_mask)
    has_digit = bool(digit_mask)
    has_special = bool(special_mask)
    
    criteria_met = has_upper and has_lower and has_digit and has_special
    
    score = 0
    if has_upper:
        score += 25
    if has_lower:
        score += 25
    if has_digit:
        score += 25
    if has_special:
        score += 25
        
    if length >= 12:
        score += 25
    elif length >= 8:
        score += 10
        
    if length >= 16:
        score += 25
        
    entropy_est = length * 3.3219280948873626 
    if has_upper:
        entropy_est += 4.700439718141093 
    if has_lower:
        entropy_est += 4.700439718141093 
    if has_digit:
        entropy_est += 3.3219280948873626 
    if has_special:
        entropy_est += 5.700439718141093 
        
    normalized_score = min(100, score)
    
    result = {
        "score": normalized_score,
        "criteria_met": criteria_met and length >= 8
    }
    
    return result

def evaluate_password_hardcoded() -> dict:
    sample_password = "Str0ng!Pass#2024"
    result = check_password_strength(sample_password)
    return result

if __name__ == '__main__':
    res = evaluate_password_hardcoded()
    print(res)