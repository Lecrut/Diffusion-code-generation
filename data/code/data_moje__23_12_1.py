def assign_letter_grade(score: float) -> str:
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
    sample_scores = [100, 91, 85, 74, 66, 55, 0, -1, 101]
    results = []
    for score in sample_scores:
        try:
            grade = assign_letter_grade(score)
            results.append(f"Score {score} -> Grade {grade}")
        except ValueError as e:
            results.append(f"Score {score} -> Error: {e}")
    for result in results:
        print(result)