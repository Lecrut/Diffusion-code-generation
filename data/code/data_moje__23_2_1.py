def get_letter_grade(score):
    if not isinstance(score, int):
        raise ValueError("Score must be an integer")
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

if __name__ == '__main__':
    sample_scores = [95, 85, 75, 65, 55, 100, 0]
    for s in sample_scores:
        print(f"Score {s}: {get_letter_grade(s)}")
    try:
        get_letter_grade(-1)
    except ValueError as e:
        print(e)
    try:
        get_letter_grade(101)
    except ValueError as e:
        print(e)