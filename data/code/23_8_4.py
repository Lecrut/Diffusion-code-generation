def grade_generator(scores):
    for score in scores:
        if not isinstance(score, (int, float)):
            continue
        if score < 0:
            continue
        if score > 100:
            continue
        if score < 60:
            yield 'F'
        elif score < 70:
            yield 'D'
        elif score < 80:
            yield 'C'
        elif score < 90:
            yield 'B'
        else:
            yield 'A'

if __name__ == '__main__':
    sample_scores = [55, 72, 88, 95, -10, 'abc', None, 100, 101, 45]
    grades = list(grade_generator(sample_scores))
    print(grades)