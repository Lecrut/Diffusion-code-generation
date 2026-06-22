def determine_grade(score):
    grade_thresholds = [
        (0, 'F'),
        (60, 'D'),
        (70, 'C'),
        (80, 'B'),
        (90, 'A')
    ]
    sorted_thresholds = sorted(grade_thresholds, key=lambda x: x[0], reverse=True)
    for threshold, grade in sorted_thresholds:
        if score >= threshold:
            return grade
    return 'F'

if __name__ == '__main__':
    sample_scores = [85, 92, 55, 78, 60]
    for s in sample_scores:
        print(determine_grade(s))