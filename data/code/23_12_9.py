def assign_grade(score: float) -> str:
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

if __name__ == '__main__':
    test_scores = [100, 95, 85, 75, 65, 55, 0, -5, 105, 60, 89.9, 90.1]
    results = [assign_grade(s) for s in test_scores]
    for score, grade in zip(test_scores, results):
        print(f"{score}: {grade}")