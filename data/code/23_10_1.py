def score_to_grade(score):
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
    print(score_to_grade(95))
    print(score_to_grade(85))
    print(score_to_grade(75))
    print(score_to_grade(65))
    print(score_to_grade(55))
    print(score_to_grade(90))
    print(score_to_grade(80))
    print(score_to_grade(70))
    print(score_to_grade(60))
    print(score_to_grade(0))
    print(score_to_grade(100))