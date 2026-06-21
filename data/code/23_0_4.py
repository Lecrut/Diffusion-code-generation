def get_grade(score):
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be an integer or a float.")
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100 inclusive.")
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
    test_scores = [95, 82, 76, 59, 45, 0, 100]
    for s in test_scores:
        print(f"Score: {s} -> Grade: {get_grade(s)}")
    try:
        get_grade(101)
    except ValueError as e:
        print(f"Error for 101: {e}")
    try:
        get_grade("A")
    except TypeError as e:
        print(f"Error for 'A': {e}")