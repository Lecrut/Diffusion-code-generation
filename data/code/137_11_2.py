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
    print(f"Score 88: {check_grade(88)}")
    print(f"Score 72: {check_grade(72)}")
    print(f"Score 60: {check_grade(60)}")
    print(f"Score 55: {check_grade(55)}")
    print(f"Score 100: {check_grade(100)}")
    print(f"Score 45: {check_grade(45)}")