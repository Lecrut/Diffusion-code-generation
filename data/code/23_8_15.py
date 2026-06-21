def grade_generator(scores):
    for score in scores:
        try:
            s = int(score)
            if 0 <= s <= 100:
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
        except (ValueError, TypeError):
            continue

if __name__ == '__main__':
    sample_scores = [95, 82, "invalid", 74, -10, "B", 60, 45, 101, 33]
    grades = list(grade_generator(sample_scores))
    print(grades)