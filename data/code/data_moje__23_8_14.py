def grade_generator(scores):
    def get_grade(score):
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
        if isinstance(score, (int, float)) and 0 <= score <= 100:
            yield get_grade(score)

if __name__ == '__main__':
    sample_scores = [95, 82, 75, 58, -5, 105, 100, 0, 'invalid', None, 88.5]
    grades = list(grade_generator(sample_scores))
    print(grades)