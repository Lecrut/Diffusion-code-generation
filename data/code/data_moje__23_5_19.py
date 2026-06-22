def calculate_grades(scores):
    if not scores:
        return []
    
    min_score = min(scores)
    max_score = max(scores)
    score_range = max_score - min_score
    
    if score_range == 0:
        return ['A' for _ in scores]
    
    grades = []
    for s in scores:
        normalized = (s - min_score) / score_range
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
    sample_scores = [85, 92, 78, 55, 100, 60, 90]
    result = calculate_grades(sample_scores)
    print(result)