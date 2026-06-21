def grade_sequence(scores):
    for score in scores:
        try:
            value = float(score)
            if 90 <= value <= 100:
                yield 'A'
            elif 80 <= value < 90:
                yield 'B'
            elif 70 <= value < 80:
                yield 'C'
            elif 60 <= value < 70:
                yield 'D'
            elif 0 <= value < 60:
                yield 'F'
        except (ValueError, TypeError):
            continue

if __name__ == '__main__':
    test_scores = [95, 82, 'invalid', 75, -10, 'N/A', 65, 55, 101, 88.5]
    for grade in grade_sequence(test_scores):
        print(grade)