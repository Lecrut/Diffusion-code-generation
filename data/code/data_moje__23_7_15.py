def get_grade_for_score(score, grade_boundaries):
    sorted_boundaries = sorted(grade_boundaries, key=lambda x: x[0], reverse=True)
    grade = next((boundary[1] for boundary in sorted_boundaries if score >= boundary[0]), 'F')
    return grade

if __name__ == '__main__':
    score = 87
    grade_boundaries = [(90, 'A'), (80, 'B'), (70, 'C'), (60, 'D'), (0, 'F')]
    print(get_grade_for_score(score, grade_boundaries))