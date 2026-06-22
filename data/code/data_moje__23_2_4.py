def get_letter_grade(score):
    if not (0 <= score <= 100):
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
    scores = [95, 85, 75, 65, 55, 0, 100]
    for s in scores:
        print(get_letter_grade(s))
    try:
        get_letter_grade(101)
    except ValueError as e:
        print(str(e))
    try:
        get_letter_grade(-1)
    except ValueError as e:
        print(str(e))