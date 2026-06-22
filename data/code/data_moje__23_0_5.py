def assign_grade(score):
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be an integer or float")
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
    test_scores = [95, 82, 75, 65, 55, 100, 0, 89.5, 79.9]
    for s in test_scores:
        print(assign_grade(s))
    try:
        assign_grade(101)
    except ValueError as e:
        print(e)
    try:
        assign_grade("A")
    except TypeError as e:
        print(e)