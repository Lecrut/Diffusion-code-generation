def score_password(password: str) -> int:
    length = len(password)
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special = True
            
    diversity = 0
    if has_lower:
        diversity += 1
    if has_upper:
        diversity += 1
    if has_digit:
        diversity += 1
    if has_special:
        diversity += 1
        
    length_score = 0
    if length >= 8:
        length_score += 2
    if length >= 12:
        length_score += 2
    if length >= 16:
        length_score += 1
        
    score = (diversity * 2) + length_score
    if score > 10:
        score = 10
    return score

if __name__ == '__main__':
    test_cases = ["abc", "abc123", "Abc123!", "MyS3cret!Passw0rd"]
    for p in test_cases:
        print(score_password(p))