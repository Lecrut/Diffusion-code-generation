def grade_generator(scores):
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
    sample_scores = [85, 92, -5, 73, 'invalid', 45, 100, 67, None, 88.5]
    grades = list(grade_generator(sample_scores))
    print(grades)