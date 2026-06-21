import re

def score_password(password: str) -> int:
    if not password:
        return 0
    
    length_score = min(len(password) // 2, 5)
    
    has_lower = bool(re.search(r'[a-z]', password))
    has_upper = bool(re.search(r'[A-Z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[^a-zA-Z0-9]', password))
    
    diversity_score = 0
    if has_lower:
        diversity_score += 1
    if has_upper:
        diversity_score += 1
    if has_digit:
        diversity_score += 1
    if has_special:
        diversity_score += 1
    
    final_score = length_score + diversity_score
    return min(final_score, 10)

if __name__ == '__main__':
    passwords = ["abc", "abc123", "Abc123!", "STRONG_P@ssw0rd_123"]
    for p in passwords:
        print(score_password(p))