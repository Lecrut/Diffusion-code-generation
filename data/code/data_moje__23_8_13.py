def grade_generator(scores):
    for score in scores:
        try:
            score_val = float(score)
            if score_val < 0 or score_val > 100:
                continue
            if score_val >= 90:
                yield 'A'
            elif score_val >= 80:
                yield 'B'
            elif score_val >= 70:
                yield 'C'
            elif score_val >= 60:
                yield 'D'
            else:
                yield 'F'
        except (TypeError, ValueError):
            continue

if __name__ == '__main__':
    sample_scores = [95, 82, 73, 65, 50, -5, 101, 'invalid', None, 88.5, 90, 60, 0, 100]
    grades = list(grade_generator(sample_scores))
    print(grades)