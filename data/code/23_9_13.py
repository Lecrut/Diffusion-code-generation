GRADE_THRESHOLDS = [(90, 'A'), (80, 'B'), (70, 'C'), (60, 'D')]
GRADE_DEFAULT = 'F'

def get_grade(score):
    return next((grade for threshold, grade in sorted(GRADE_THRESHOLDS, key=lambda x: x[0], reverse=True) if score >= threshold), GRADE_DEFAULT)

if __name__ == '__main__':
    print(get_grade(95))
    print(get_grade(85))
    print(get_grade(75))
    print(get_grade(65))
    print(get_grade(55))