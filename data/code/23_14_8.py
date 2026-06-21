def get_grade(score: float, thresholds: dict | None = None) -> str:
    if thresholds is None:
        thresholds = {
            'A': 90,
            'B': 80,
            'C': 70,
            'D': 60,
        }
    
    sorted_thresholds = sorted(thresholds.items(), key=lambda x: x[1], reverse=True)
    
    for grade, threshold in sorted_thresholds:
        if score >= threshold:
            return grade
    
    return 'F'

if __name__ == '__main__':
    print(get_grade(92))