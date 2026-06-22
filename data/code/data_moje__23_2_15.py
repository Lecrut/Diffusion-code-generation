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
    print(get_letter_grade(95))
    print(get_letter_grade(85))
    print(get_letter_grade(75))
    print(get_letter_grade(65))
    print(get_letter_grade(55))
    print(get_letter_grade(0))
    print(get_letter_grade(100))
    try:
        get_letter_grade(101)
    except ValueError as e:
        print(e)
    try:
        get_letter_grade(-1)
    except ValueError as e:
        print(e)