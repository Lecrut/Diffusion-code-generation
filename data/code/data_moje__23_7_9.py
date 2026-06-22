def determine_grade(score):
    grades = [(90, 'A'), (80, 'B'), (70, 'C'), (60, 'D'), (0, 'F')]
    grades_sorted = sorted(grades, key=lambda x: x[0], reverse=True)
    for threshold, grade in grades_sorted:
        if score >= threshold:
            return grade
    return 'F'

if __name__ == '__main__':
    print(determine_grade(85))
    print(determine_grade(95))
    print(determine_grade(72))
    print(determine_grade(55))