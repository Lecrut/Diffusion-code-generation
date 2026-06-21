def grade_generator(scores):
    for score in scores:
        try:
            value = int(score)
            if not 0 <= value <= 100:
                continue
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
    sample_scores = [95, 82, 74, 61, 55, "invalid", -5, 105, 3.5, "ABC", 50]
    grades = list(grade_generator(sample_scores))
    print(grades)