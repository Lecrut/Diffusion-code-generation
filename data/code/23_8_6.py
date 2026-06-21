def grade_generator(scores):
    valid_thresholds = [(0, 60, "F"), (60, 70, "D"), (70, 80, "C"), (80, 90, "B"), (90, 100, "A")]
    for score in scores:
        try:
            value = float(score)
            if not (0 <= value <= 100):
                continue
            for low, high, grade in valid_thresholds:
                if low <= value < high or (low == 90 and value == 100):
                    yield grade
                    break
        except (TypeError, ValueError):
            continue

if __name__ == '__main__':
    sample_scores = [85, "92", 55.5, "invalid", 105, 78, None, 90]
    grades = list(grade_generator(sample_scores))
    print(grades)