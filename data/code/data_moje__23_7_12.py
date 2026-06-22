def determine_grade(score, grade_scale=None):
    if grade_scale is None:
        grade_scale = [
            (0, "F"),
            (50, "D"),
            (60, "C"),
            (70, "B"),
            (80, "A"),
            (90, "A+")
        ]
    sorted_scale = sorted(grade_scale, key=lambda x: x[0])
    grade = "F"
    for min_score, label in sorted_scale:
        if score >= min_score:
            grade = label
        else:
            break
    return grade

if __name__ == '__main__':
    sample_scores = [45, 55, 65, 75, 85, 95]
    for s in sample_scores:
        print(determine_grade(s))