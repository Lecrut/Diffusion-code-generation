def score_to_grade(score):
    if not isinstance(score, int):
        raise TypeError("Score must be an integer")
    if score < 0:
        return "F"
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"

if __name__ == '__main__':
    test_scores = [95, 82, 70, 60, 59, 0, -5]
    for s in test_scores:
        print(f"Score {s}: {score_to_grade(s)}")