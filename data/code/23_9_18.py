THRESHOLDS = [60, 70, 80, 90]
GRADES = 'FDCBA'

def get_grade(score):
    return GRADES[next((i for i, t in enumerate(THRESHOLDS) if score >= t), 0)]

if __name__ == '__main__':
    print(get_grade(95))
    print(get_grade(82))
    print(get_grade(60))
    print(get_grade(59))