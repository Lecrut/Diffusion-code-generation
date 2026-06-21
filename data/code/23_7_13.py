from functools import cmp_to_key

def get_grade(score, grade_boundaries):
    sorted_boundaries = sorted(grade_boundaries, key=lambda x: x[0], reverse=True)
    for boundary_score, grade in sorted_boundaries:
        if score >= boundary_score:
            return grade
    return sorted_boundaries[-1][1]

if __name__ == '__main__':
    boundaries = [(90, 'A'), (80, 'B'), (70, 'C'), (60, 'D'), (0, 'F')]
    test_score = 85
    result = get_grade(test_score, boundaries)
    print(result)