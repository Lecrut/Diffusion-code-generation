def get_grade(score):
    score_grades = [
        (100, 'A+'),
        (90, 'A'),
        (85, 'A-'),
        (80, 'B+'),
        (75, 'B'),
        (70, 'B-'),
        (65, 'C+'),
        (60, 'C'),
        (50, 'D'),
        (0, 'F')
    ]
    score_grades_sorted = sorted(score_grades, key=lambda x: x[0], reverse=True)
    for threshold, grade in score_grades_sorted:
        if score >= threshold:
            return grade
    return 'F'

if __name__ == '__main__':
    print(get_grade(85))