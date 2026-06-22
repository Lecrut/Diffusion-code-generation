def get_grade(score):
    score_grade_pairs = [
        (90, 'A'),
        (80, 'B'),
        (70, 'C'),
        (60, 'D'),
        (0, 'F')
    ]
    
    sorted_scores = sorted(score_grade_pairs, key=lambda x: x[0], reverse=True)
    
    grade = sorted_scores[-1][1]
    for threshold, g in sorted_scores:
        if score >= threshold:
            grade = g
            break
            
    return grade

if __name__ == '__main__':
    scores = [95, 82, 70, 59, 0, 100]
    results = [get_grade(s) for s in scores]
    print(results)