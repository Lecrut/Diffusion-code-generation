def generate_grades(scores):
    for score in scores:
        if not isinstance(score, (int, float)):
            continue
        if score < 0:
            continue
        if score > 100:
            continue
        if 90 <= score <= 100:
            yield 'A'
        elif 80 <= score < 90:
            yield 'B'
        elif 70 <= score < 80:
            yield 'C'
        elif 60 <= score < 70:
            yield 'D'
        else:
            yield 'F'

if __name__ == '__main__':
    sample_scores = [95, 82, 55, 'invalid', -10, 101, 70, 65]
    grades = list(generate_grades(sample_scores))
    print(grades)