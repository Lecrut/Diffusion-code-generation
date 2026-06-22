def get_grade(score, score_grade_pairs=None):
    if score_grade_pairs is None:
        score_grade_pairs = [
            (90, 'A'),
            (80, 'B'),
            (70, 'C'),
            (60, 'D'),
            (0, 'F')
        ]
    sorted_pairs = sorted(score_grade_pairs, key=lambda x: x[0], reverse=True)
    for threshold, grade in sorted_pairs:
        if score >= threshold:
            return grade
    return 'F'

if __name__ == '__main__':
    print(get_grade(85))
    print(get_grade(55))
    print(get_grade(92))