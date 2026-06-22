SCORE_CAP = 10

def evaluate_password_strength(candidate: str) -> int:
    if not candidate:
        return 0
    
    length_bonus = min(len(candidate), SCORE_CAP)
    
    character_categories = {'lower': False, 'upper': False, 'digit': False, 'other': False}
    
    for char in candidate:
        if char in 'abcdefghijklmnopqrstuvwxyz':
            character_categories['lower'] = True
        elif char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            character_categories['upper'] = True
        elif char in '0123456789':
            character_categories['digit'] = True
        else:
            character_categories['other'] = True
            
    diversity_points = 0
    if character_categories['lower']:
        diversity_points += 2
    if character_categories['upper']:
        diversity_points += 2
    if character_categories['digit']:
        diversity_points += 2
    if character_categories['other']:
        diversity_points += 2
        
    total_raw = length_bonus + diversity_points
    
    if total_raw > SCORE_CAP:
        return SCORE_CAP
    return total_raw

if __name__ == '__main__':
    sample_password = "Str0ng!Pass"
    result = evaluate_password_strength(sample_password)
    print(result)