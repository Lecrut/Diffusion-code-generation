def get_grade(score: float, thresholds: list = None) -> str:
    if thresholds is None:
        thresholds = [(90, 'A'), (80, 'B'), (70, 'C'), (60, 'D'), (0, 'F')]
    
    for threshold, grade in thresholds:
        if score >= threshold:
            return grade
    return 'F'

if __name__ == '__main__':
    score = 92
    result = get_grade(score)
    print(result)