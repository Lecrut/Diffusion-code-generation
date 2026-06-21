def get_letter_grade(score):
    if not isinstance(score, int) or not (0 <= score <= 100):
        raise ValueError("Score must be an integer between 0 and 100")
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
    scores = [95, 82, 70, 58, 100, 0]
    for s in scores:
        print(get_letter_grade(s))