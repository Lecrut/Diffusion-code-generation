def check_grade(score):
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
    print(check_grade(95))
    print(check_grade(82))
    print(check_grade(77))
    print(check_grade(60))
    print(check_grade(55))