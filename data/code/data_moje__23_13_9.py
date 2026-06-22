import bisect

def get_grading_scale():
    thresholds = [0, 60, 70, 80, 90, 100]
    grades = ['F', 'D', 'C', 'B', 'A']
    return thresholds, grades

def get_grade(score, thresholds, grades):
    pos = bisect.bisect_right(thresholds, score) - 1
    if pos < 0:
        return grades[0]
    if pos >= len(grades):
        return grades[-1]
    return grades[pos]

def lookup_grade(score):
    thresholds, grades = get_grading_scale()
    return get_grade(score, thresholds, grades)

if __name__ == '__main__':
    sample_score = 85
    result = lookup_grade(sample_score)
    print(result)