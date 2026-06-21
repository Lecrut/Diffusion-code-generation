GRADING_MAP = {
    90: 'A',
    80: 'B',
    70: 'C',
    60: 'D',
    0: 'F'
}

def get_grade(score):
    for threshold in sorted(GRADING_MAP.keys(), reverse=True):
        if score >= threshold:
            return GRADING_MAP[threshold]
    return 'F'

if __name__ == '__main__':
    print(get_grade(100))
    print(get_grade(92))
    print(get_grade(81))
    print(get_grade(74))
    print(get_grade(63))
    print(get_grade(49))
    print(get_grade(10))