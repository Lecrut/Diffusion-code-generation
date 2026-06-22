def scores_to_letter_grades(scores):
    grade_bounds = (
        (90, 100, 'A'),
        (80, 89, 'B'),
        (70, 79, 'C'),
        (60, 69, 'D'),
        (0, 59, 'F'),
    )
    grade_map = {score: grade for low, high, grade in grade_bounds for score in range(low, high + 1)}
    return [grade_map[score] for score in scores]

if __name__ == '__main__':
    sample_scores = [95, 82, 77, 65, 50, 100, 0, 89, 70, 60]
    print(scores_to_letter_grades(sample_scores))