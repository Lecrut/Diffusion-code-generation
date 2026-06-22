import math

def compute_grades(scores):
    if not scores:
        return []
    
    max_score = max(scores)
    min_score = min(scores)
    score_range = max_score - min_score
    
    if score_range == 0:
        return ['A' for _ in scores]
    
    grades = []
    for score in scores:
        if max_score == 0 and min_score == 0:
            grades.append('A')
            continue
            
        normalized = (score - min_score) / score_range
        
        if normalized >= 0.9:
            grades.append('A')
        elif normalized >= 0.8:
            grades.append('B')
        elif normalized >= 0.7:
            grades.append('C')
        elif normalized >= 0.6:
            grades.append('D')
        else:
            grades.append('F')
            
    return grades

if __name__ == '__main__':
    sample_scores = [95, 88, 72, 65, 50]
    result = compute_grades(sample_scores)
    print(result)