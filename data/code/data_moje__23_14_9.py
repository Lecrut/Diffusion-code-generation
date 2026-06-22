def get_grade(score: float, thresholds: tuple = None) -> str:
    if thresholds is None:
        thresholds = ((90, 'A'), (80, 'B'), (70, 'C'), (60, 'D'))
    for threshold, grade in thresholds:
        if score >= threshold:
            return grade
    return 'F'

if __name__ == '__main__':
    print(get_grade(92))