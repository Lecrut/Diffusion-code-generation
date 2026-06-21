def score_to_grade(score):
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

if __name__ == '__main__':
    test_scores = [95, 85, 75, 65, 55, 0, 100, 89, 79, 69, 60, 59]
    for s in test_scores:
        print(f"Score {s} -> Grade {score_to_grade(s)}")