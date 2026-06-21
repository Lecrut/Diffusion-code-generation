def get_letter_grade(score):
    if not 0 <= score <= 100:
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
    test_scores = [95, 82, 76, 64, 55, 101, -5]
    for s in test_scores:
        try:
            print(get_letter_grade(s))
        except ValueError as e:
            print(f"Error for {s}: {e}")