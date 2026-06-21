def get_grade(score: float, thresholds: dict = None) -> str:
    if thresholds is None:
        thresholds = {
            'A': 90,
            'B': 80,
            'C': 70,
            'D': 60,
            'F': 0
        }
    
    sorted_thresholds = sorted(thresholds.items(), key=lambda x: x[1], reverse=True)
    
    for grade, threshold in sorted_thresholds:
        if score >= threshold:
            return grade
    
    return 'F'

if __name__ == '__main__':
    score = 92
    grade = get_grade(score)
    print(grade)