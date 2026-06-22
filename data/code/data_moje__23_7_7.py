def get_grade_for_score(score):
    grades = sorted(
        [(90, "A"), (80, "B"), (70, "C"), (60, "D"), (0, "F")],
        key=lambda x: x[0],
        reverse=True
    )
    for threshold, grade in grades:
        if score >= threshold:
            return grade
    return "F"

if __name__ == '__main__':
    print(get_grade_for_score(85))
    print(get_grade_for_score(72))
    print(get_grade_for_score(91))
    print(get_grade_for_score(55))