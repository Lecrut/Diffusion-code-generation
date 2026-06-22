def get_letter_grade(score):
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

if __name__ == "__main__":
    test_scores = [100, 90, 85, 72, 61, 45, 0, 99.9]
    for s in test_scores:
        print(get_letter_grade(s))
    try:
        print(get_letter_grade(-5))
    except ValueError:
        print("ValueError caught for -5")
    try:
        print(get_letter_grade("A"))
    except TypeError:
        print("TypeError caught for 'A'")