def score_to_grade(score: float) -> str:
    if score >= 90.0:
        return 'A'
    elif score >= 80.0:
        return 'B'
    elif score >= 70.0:
        return 'C'
    elif score >= 60.0:
        return 'D'
    else:
        return 'F'
if __name__ == '__main__':
    sample_scores = [95.5, 88.0, 72.3, 60.0, 59.9, 0.0, 100.0, 45.7]
    for s in sample_scores:
        print(f'Score: {s}, Grade: {score_to_grade(s)}')