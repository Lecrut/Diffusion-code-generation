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
    print(get_letter_grade(82))
    print(get_letter_grade(76))
    print(get_letter_grade(64))
    print(get_letter_grade(58))