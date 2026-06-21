def grade_generator(scores):
    def compute_grade(score):
        try:
            score = float(score)
        except (TypeError, ValueError):
            return None
        if score < 0 or score > 100:
            return None
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'

    for score in scores:
        grade = compute_grade(score)
        if grade is not None:
            yield grade

if __name__ == '__main__':
    sample_scores = [95, 87, 'invalid', 72, -5, 65, 101, 88.5, None, 90, 69.9]
    grades = list(grade_generator(sample_scores))
    print(grades)