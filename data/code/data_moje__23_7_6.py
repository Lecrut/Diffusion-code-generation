def get_grade(score, grade_boundaries):
    sorted_boundaries = sorted(grade_boundaries, key=lambda x: x[0])
    grade = sorted_boundaries[-1][1]
    for min_score, g in sorted_boundaries:
        if score >= min_score:
            grade = g
        else:
            break
    return grade
if __name__ == '__main__':
    grade_boundaries = [(0, 'F'), (60, 'D'), (70, 'C'), (80, 'B'), (90, 'A')]
    test_scores = [55, 65, 75, 85, 95]
    results = [get_grade(score, grade_boundaries) for score in test_scores]
    print(results)