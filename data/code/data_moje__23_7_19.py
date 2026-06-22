def get_grade_for_score(score, grade_boundaries):
    sorted_boundaries = sorted(grade_boundaries, key=lambda x: x[0], reverse=True)
    grade = sorted_boundaries[-1][1]
    for boundary, letter_grade in sorted_boundaries:
        if score >= boundary:
            grade = letter_grade
            break
    return grade

if __name__ == '__main__':
    grade_boundaries = [(90, 'A'), (80, 'B'), (70, 'C'), (60, 'D'), (0, 'F')]
    sample_scores = [95, 85, 75, 65, 55]
    results = [get_grade_for_score(s, grade_boundaries) for s in sample_scores]
    print(results)