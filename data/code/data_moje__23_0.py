def assign_grade(score):
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a number")
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100 inclusive")
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
    sample_scores = [100, 95, 88, 73, 65, 59, 0, 90, 80, 70, 60, 45]
    results = []
    for s in sample_scores:
        results.append((s, assign_grade(s)))
    print(results)