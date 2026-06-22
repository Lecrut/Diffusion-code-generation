def score_password(password):
    length = len(password)
    if length == 0:
        return 0
    
    length_score = min(length * 2, 10)
    
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    
    diversity_count = sum([has_lower, has_upper, has_digit, has_special])
    
    if diversity_count == 0:
        diversity_score = 0
    elif diversity_count == 1:
        diversity_score = 2
    elif diversity_count == 2:
        diversity_score = 5
    elif diversity_count == 3:
        diversity_score = 8
    else:
        diversity_score = 10
    
    total_score = min(length_score + diversity_score, 10)
    
    if length < 8:
        total_score = max(0, total_score - (8 - length) * 2)
    
    return min(10, max(0, total_score))

if __name__ == '__main__':
    print(score_password("Str0ng!Pass#1"))
    print(score_password("weak"))
    print(score_password("AllLowercase1"))