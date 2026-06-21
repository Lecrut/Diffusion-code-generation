def assign_grade(score):
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a numeric type")
    if score < 0:
        return 'F'
    if score > 100:
        return 'F'
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
    print(assign_grade(95))
    print(assign_grade(85))
    print(assign_grade(75))
    print(assign_grade(65))
    print(assign_grade(55))
    print(assign_grade(100))
    print(assign_grade(0))
    print(assign_grade(-1))
    print(assign_grade(101))