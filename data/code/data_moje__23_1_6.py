def scores_to_letter_grades(raw_scores):
    grade_boundaries = [
        (90, "A"),
        (80, "B"),
        (70, "C"),
        (60, "D"),
        (0, "F")
    ]
    return [
        next(
            grade
            for threshold, grade in grade_boundaries
            if score >= threshold
        )
        for score in raw_scores
    ]

if __name__ == '__main__':
    sample_scores = [95, 87, 72, 68, 59, 40, 90, 80, 70, 60]
    print(scores_to_letter_grades(sample_scores))