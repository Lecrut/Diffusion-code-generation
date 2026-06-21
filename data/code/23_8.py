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
    sample_scores = [95, 'invalid', 85, -1, 72, None, 55, 100]
    grades = list(yield_grades(sample_scores))
    print(grades)