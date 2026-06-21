def assign_grade(score):
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a number")
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
    if score >= 90:
        return 'A'
    if score >= 80:
        return 'B'
    if score >= 70:
        return 'C'
    if score >= 60:
        return 'D'
    return 'F'

if __name__ == '__main__':
    sample_scores = [95, 87, 72, 65, 58, 0, 100, 89.9, 60.1]
    for s in sample_scores:
        print(f"Score {s}: {assign_grade(s)}")