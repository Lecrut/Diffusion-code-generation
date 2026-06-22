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
    samples = [95, 82, 76, 55, "invalid", None, 101, -5, 60, 45]
    grades = list(grade_generator(samples))
    print(grades)