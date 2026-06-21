def assign_grade(score):
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a number")
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100 inclusive")
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
    print(assign_grade(95))
    print(assign_grade(85))
    print(assign_grade(75))
    print(assign_grade(65))
    print(assign_grade(55))
    print(assign_grade(90))
    print(assign_grade(80))
    print(assign_grade(70))
    print(assign_grade(60))
    print(assign_grade(0))
    print(assign_grade(100))