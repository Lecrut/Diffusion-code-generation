def get_grade(score):
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a number")
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
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
    test_scores = [95, 85, 75, 65, 55, 100, 0]
    for s in test_scores:
        print(get_grade(s))
    try:
        print(get_grade(101))
    except ValueError as e:
        print(e)
    try:
        print(get_grade("A"))
    except TypeError as e:
        print(e)