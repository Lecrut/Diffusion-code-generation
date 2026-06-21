def get_grade(score, grade_levels):
    grade_levels_sorted = sorted(grade_levels, key=lambda x: x[1])
    for grade_name, threshold in grade_levels_sorted:
        if score >= threshold:
            return grade_name
    return grade_levels_sorted[0][0]

if __name__ == '__main__':
    grades = [('A', 90), ('B', 80), ('C', 70), ('D', 60), ('F', 0)]
    test_score = 85
    result = get_grade(test_score, grades)
    print(result)