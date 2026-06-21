def assign_grade(score):
    if not isinstance(score, (int, float)) or score < 0 or score > 100:
        raise ValueError("Score must be a number between 0 and 100.")
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
    test_scores = [95, 82, 74, 61, 55, 0, 100, 89.5, 69.9]
    for s in test_scores:
        print(f"{s}: {assign_grade(s)}")
    try:
        assign_grade(-1)
    except ValueError as e:
        print(f"Error: {e}")
    try:
        assign_grade(101)
    except ValueError as e:
        print(f"Error: {e}")