def get_grade(score: float) -> str:
    score_grade_pairs = [
        (100, 'A+'),
        (90, 'A'),
        (80, 'B'),
        (70, 'C'),
        (60, 'D'),
        (0, 'F')
    ]
    sorted_pairs = sorted(score_grade_pairs, key=lambda x: x[0], reverse=True)
    grade = sorted_pairs[-1][1]
    for min_score, g in sorted_pairs:
        if score >= min_score:
            grade = g
            break
    return grade

if __name__ == '__main__':
    scores = [85.5, 92.0, 59.9, 100, 70, 45]
    results = [get_grade(s) for s in scores]
    print(results)