def score_password(password: str) -> int:
    length = len(password)
    if length == 0:
        return 0
    
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    
    special_chars = set("!@#$%^&*()_+-=[]{}|;:,.<>?/~`")
    
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True
    
    diversity_score = 0
    if has_lower:
        diversity_score += 1
    if has_upper:
        diversity_score += 1
    if has_digit:
        diversity_score += 1
    if has_special:
        diversity_score += 1
    
    length_score = 0
    if length >= 8:
        length_score += 1
    if length >= 12:
        length_score += 1
    if length >= 16:
        length_score += 1
    if length >= 20:
        length_score += 1
    
    total = (diversity_score * 2) + (length_score * 1)
    
    if total > 10:
        total = 10
    
    return total

if __name__ == '__main__':
    samples = [
        "abc",
        "abcdef",
        "Abcdef1",
        "Abcdefgh1!",
        "Abcdefgh1!Xy",
        "Short1!",
        "VeryLongComplexPassword123!@#"
    ]
    for s in samples:
        print(score_password(s))