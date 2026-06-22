def get_grade(score, grade_boundaries):
    grades = ['F', 'E', 'D', 'C', 'B', 'A']
    for threshold, grade in sorted(grade_boundaries, key=lambda x: x[0], reverse=True):
        if score >= threshold:
            return grade
    return 'F'

if __name__ == '__main__':
    boundaries = [(90, 'A'), (80, 'B'), (70, 'C'), (60, 'D'), (50, 'E'), (40, 'F')]
    result = get_grade(85, boundaries)
    print(result)