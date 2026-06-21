def grade_generator(scores):
    for score in scores:
        try:
            score_num = float(score)
            if score_num < 0 or score_num > 100:
                continue
            if score_num >= 90:
                yield 'A'
            elif score_num >= 80:
                yield 'B'
            elif score_num >= 70:
                yield 'C'
            elif score_num >= 60:
                yield 'D'
            else:
                yield 'F'
        except (TypeError, ValueError):
            continue

if __name__ == '__main__':
    sample_scores = [95, 82, 75, 60, 55, -10, "invalid", 101, 88.5, None, 100, 0]
    grades = list(grade_generator(sample_scores))
    print(grades)