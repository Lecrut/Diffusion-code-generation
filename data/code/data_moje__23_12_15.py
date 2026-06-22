def assign_grade(score):
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
    print(assign_grade(85))
    print(assign_grade(72))
    print(assign_grade(95))
    print(assign_grade(59))