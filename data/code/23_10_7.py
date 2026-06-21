def get_grade(score):
    if score < 0:
        return 'F'
    elif score < 60:
        return 'F'
    elif score < 70:
        return 'D'
    elif score < 80:
        return 'C'
    elif score < 90:
        return 'B'
    else:
        return 'A'

if __name__ == '__main__':
    print(get_grade(95))
    print(get_grade(82))
    print(get_grade(76))
    print(get_grade(64))
    print(get_grade(55))