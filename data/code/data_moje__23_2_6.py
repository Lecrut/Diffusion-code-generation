def get_letter_grade(score):
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
    print(get_letter_grade(95))
    print(get_letter_grade(82))
    print(get_letter_grade(74))
    print(get_letter_grade(65))
    print(get_letter_grade(58))
    print(get_letter_grade(0))
    print(get_letter_grade(100))
    try:
        print(get_letter_grade(-1))
    except ValueError:
        print('ValueError')
    try:
        print(get_letter_grade(101))
    except ValueError:
        print('ValueError')