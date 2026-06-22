import re
import hashlib
import unicodedata

def validate_password_strength(password):
    errors = []
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")
    
    upper_count = sum(1 for c in password if c.isupper())
    lower_count = sum(1 for c in password if c.islower())
    digit_count = sum(1 for c in password if c.isdigit())
    special_count = sum(1 for c in password if not c.isalnum())
    
    if upper_count < 1:
        errors.append("Password must contain at least one uppercase letter.")
    if lower_count < 1:
        errors.append("Password must contain at least one lowercase letter.")
    if digit_count < 1:
        errors.append("Password must contain at least one digit.")
    if special_count < 1:
        errors.append("Password must contain at least one special character.")
    
    common_passwords = [
        "password", "123456", "12345678", "qwerty", "abc123", 
        "monkey", "master", "dragon", "111111", "baseball",
        "iloveyou", "trustno1", "sunshine", "princess", "football",
        "shadow", "superman", "michael", "password1", "qwerty123"
    ]
    
    normalized = unicodedata.normalize('NFKD', password).encode('ASCII', 'ignore').decode('ASCII').lower()
    
    if normalized in common_passwords:
        errors.append("Password is too common.")
    
    for i in range(len(normalized) - 2):
        substr = normalized[i:i+3]
        if len(set(substr)) == 1:
            errors.append("Password contains sequential repeated characters.")
            break
        if i > 0:
            prev_ord = ord(normalized[i-1])
            curr_ord = ord(substr[0])
            next_ord = ord(substr[2]) if i < len(normalized) - 2 else None
            if next_ord is not None and abs(curr_ord - prev_ord) == 1 and abs(next_ord - curr_ord) == 1:
                seq_count = 1
                if curr_ord - prev_ord == next_ord - curr_ord:
                    seq_count = 3
                    j = i + 3
                    while j < len(normalized) and ord(normalized[j]) - ord(normalized[j-1]) == curr_ord - prev_ord:
                        seq_count += 1
                        j += 1
                    if seq_count >= 3:
                        errors.append("Password contains sequential characters.")
                        break
    
    unique_ratio = len(set(password)) / len(password) if password else 0
    if unique_ratio < 0.5:
        errors.append("Password has too many repeated characters.")
        
    if not errors:
        return {"is_valid": True, "score": 100, "errors": []}
    
    score = 100
    if len(errors) > 0:
        score -= len(errors) * 10
    if score < 0:
        score = 0
        
    return {"is_valid": False, "score": score, "errors": errors}

if __name__ == '__main__':
    test_passwords = ["Str0ng!Pass", "short", "password123", "AllUppercase!1", "aaabbbccc!1"]
    for pwd in test_passwords:
        result = validate_password_strength(pwd)
        print(result)