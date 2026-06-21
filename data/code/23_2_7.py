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
    print(get_letter_grade(95))
    print(get_letter_grade(82))
    print(get_letter_grade(71))
    print(get_letter_grade(65))
    print(get_letter_grade(40))
    try:
        print(get_letter_grade(101))
    except ValueError as e:
        print(e)
    try:
        print(get_letter_grade(-5))
    except ValueError as e:
        print(e)