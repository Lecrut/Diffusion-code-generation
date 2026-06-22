def get_grade(score):
    return 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'D' if score >= 60 else 'F'

if __name__ == '__main__':
    print(get_grade(95))
    print(get_grade(82))
    print(get_grade(75))
    print(get_grade(65))
    print(get_grade(45))