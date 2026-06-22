def get_grade(score, grading_scale=None):
    if grading_scale is None:
        grading_scale = [
            (90, 'A'),
            (80, 'B'),
            (70, 'C'),
            (60, 'D'),
            (0, 'F')
        ]
    sorted_scale = sorted(grading_scale, key=lambda x: x[0], reverse=True)
    for threshold, grade in sorted_scale:
        if score >= threshold:
            return grade
    return 'F'

if __name__ == '__main__':
    sample_scores = [95, 82, 71, 59, 45]
    for s in sample_scores:
        print(get_grade(s))