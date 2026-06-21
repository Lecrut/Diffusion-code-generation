import string

def check_password_strength(password: str) -> dict:
    required_lengths = 12
    length_score = 1 if len(password) >= required_lengths else 0
    
    lower_mask = 0
    upper_mask = 0
    digit_mask = 0
    special_mask = 0
    
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    for char in password:
        if 'a' <= char <= 'z':
            lower_mask |= 1
        elif 'A' <= char <= 'Z':
            upper_mask |= 1
        elif '0' <= char <= '9':
            digit_mask |= 1
        else:
            for spec in special_chars:
                if char == spec:
                    special_mask |= 1
                    break
    
    has_lower = (lower_mask & 1) == 1
    has_upper = (upper_mask & 1) == 1
    has_digit = (digit_mask & 1) == 1
    has_special = (special_mask & 1) == 1
    
    criteria_met = 0
    criteria_met += 1 if has_lower else 0
    criteria_met += 1 if has_upper else 0
    criteria_met += 1 if has_digit else 0
    criteria_met += 1 if has_special else 0
    criteria_met += length_score
    
    is_strong = (criteria_met == 5) and (len(password) >= 12)
    
    return {
        "length": len(password),
        "has_lower": has_lower,
        "has_upper": has_upper,
        "has_digit": has_digit,
        "has_special": has_special,
        "criteria_met": criteria_met,
        "is_strong": is_strong
    }

if __name__ == '__main__':
    test_password = "SecureP@ssw0rd123!"
    result = check_password_strength(test_password)
    print(result)