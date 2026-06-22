def assign_letter_grade(score):
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
    print(assign_letter_grade(95))
    print(assign_letter_grade(85))
    print(assign_letter_grade(75))
    print(assign_letter_grade(65))
    print(assign_letter_grade(55))
    print(assign_letter_grade(100))
    print(assign_letter_grade(0))
    print(assign_letter_grade(90))
    print(assign_letter_grade(89))
    print(assign_letter_grade(60))