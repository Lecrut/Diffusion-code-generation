def score_password_strength(password):
    length = len(password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    
    diversity_score = 0
    if has_lower:
        diversity_score += 2
    if has_upper:
        diversity_score += 2
    if has_digit:
        diversity_score += 2
    if has_special:
        diversity_score += 2
        
    length_score = 0
    if length >= 8:
        length_score += 3
    elif length >= 5:
        length_score += 2
    elif length >= 3:
        length_score += 1
        
    total_score = diversity_score + length_score
    return min(10, total_score)

if __name__ == '__main__':
    print(score_password_strength("abc"))
    print(score_password_strength("Abc123!"))
    print(score_password_strength("StrongP@ssw0rd123"))