import re

def score_password(password: str) -> int:
    length = len(password)
    
    if length < 1:
        return 0
    
    score = 0
    
    if length >= 4:
        score += 1
    if length >= 8:
        score += 2
    if length >= 12:
        score += 1
        
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'\d', password):
        score += 1
    if re.search(r'[^a-zA-Z0-9]', password):
        score += 1
        
    return min(score, 10)

if __name__ == '__main__':
    print(score_password("StrongP@ssw0rd"))