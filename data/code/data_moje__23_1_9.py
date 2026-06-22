def scores_to_grades(scores):
    grade_boundaries = [
        (90, 'A'),
        (80, 'B'),
        (70, 'C'),
        (60, 'D'),
        (0, 'F')
    ]

    def get_grade(score):
        return next(
            grade for threshold, grade in grade_boundaries if score >= threshold
        )

    return [get_grade(score) for score in scores]

if __name__ == '__main__':
    sample_scores = [95, 82, 75, 60, 55, 100, 0, 45, 89, 70]
    print(scores_to_grades(sample_scores))