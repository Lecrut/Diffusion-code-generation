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
    print(f"Score 95: {check_grade(95)}")
    print(f"Score 82: {check_grade(82)}")
    print(f"Score 70: {check_grade(70)}")
    print(f"Score 65: {check_grade(65)}")
    print(f"Score 55: {check_grade(55)}")
    print(f"Score 90: {check_grade(90)}")
    print(f"Score 40: {check_grade(40)}")