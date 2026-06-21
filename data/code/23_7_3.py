def get_grade(score, grade_boundaries):
    return next((grade for score_val, grade in reversed(grade_boundaries) if score >= score_val), 'F')

if __name__ == '__main__':
    grades = [(90, 'A'), (80, 'B'), (70, 'C'), (60, 'D'), (0, 'F')]
    test_scores = [95, 85, 75, 65, 55]
    results = [get_grade(s, grades) for s in test_scores]
    print(results)