def get_grade(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"

if __name__ == '__main__':
    print(get_grade(95))
    print(get_grade(82))
    print(get_grade(75))
    print(get_grade(61))
    print(get_grade(55))