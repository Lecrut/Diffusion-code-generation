def yield_grades(scores):
    for score in scores:
        if not isinstance(score, (int, float)):
            continue
        if score < 0 or score > 100:
            continue
        if score >= 90:
            yield 'A'
        elif score >= 80:
            yield 'B'
        elif score >= 70:
            yield 'C'
        elif score >= 60:
            yield 'D'
        else:
            yield 'F'

if __name__ == '__main__':
    sample_scores = [95, 82, 'invalid', 76, -5, 105, 55, 88]
    grades = list(yield_grades(sample_scores))
    print(grades)