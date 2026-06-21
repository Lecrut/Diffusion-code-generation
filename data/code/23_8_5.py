def grade_generator(scores):
    for score in scores:
        try:
            s = float(score)
            if s < 0 or s > 100:
                continue
            if s >= 90:
                yield 'A'
            elif s >= 80:
                yield 'B'
            elif s >= 70:
                yield 'C'
            elif s >= 60:
                yield 'D'
            else:
                yield 'F'
        except (TypeError, ValueError):
            continue

if __name__ == '__main__':
    sample_scores = [95, 82, 75, 60, 55, -10, 'invalid', 101, 88.5, 70, None, 65.0]
    grades = list(grade_generator(sample_scores))
    print(grades)