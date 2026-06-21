def get_grade(score, grade_boundaries):
    sorted_boundaries = sorted(grade_boundaries, key=lambda x: x[1], reverse=True)
    for grade, cutoff in sorted_boundaries:
        if score >= cutoff:
            return grade
    return sorted_boundaries[-1][0]

if __name__ == '__main__':
    boundaries = [('A', 90), ('B', 80), ('C', 70), ('D', 60), ('F', 0)]
    test_score = 85
    result = get_grade(test_score, boundaries)
    print(result)