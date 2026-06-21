def determine_grade(score: float, thresholds: tuple = ((90, 'A'), (80, 'B'), (70, 'C'), (60, 'D'))) -> str:
    for threshold, grade in thresholds:
        if score >= threshold:
            return grade
    return 'F'

if __name__ == '__main__':
    result = determine_grade(92)
    print(result)