def grade_generator(scores):
    for score in scores:
        try:
            value = float(score)
            if 0 <= value <= 100:
                if value >= 90:
                    yield 'A'
                elif value >= 80:
                    yield 'B'
                elif value >= 70:
                    yield 'C'
                elif value >= 60:
                    yield 'D'
                else:
                    yield 'F'
        except (ValueError, TypeError):
            continue

if __name__ == '__main__':
    sample_scores = [95, 'invalid', 82, 74.5, 'N/A', 55, 100, -10, 0]
    grades = list(grade_generator(sample_scores))
    print(grades)