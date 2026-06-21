def score_to_grade(score):
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
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
    sample_scores = [95, 87, 72, 65, 58, 100, 0, 89, 79, 60]
    results = {}
    for score in sample_scores:
        results[score] = score_to_grade(score)
    print(results)