def get_grade(score):
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
    print(get_grade(95))
    print(get_grade(85))
    print(get_grade(75))
    print(get_grade(65))
    print(get_grade(55))
    try:
        print(get_grade(101))
    except ValueError as e:
        print(repr(e))
    try:
        print(get_grade(-1))
    except ValueError as e:
        print(repr(e))