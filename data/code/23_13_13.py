import bisect

def get_grading_scale():
    thresholds = [0, 60, 70, 80, 90, 100]
    grades = ['F', 'D', 'C', 'B', 'A']
    return thresholds, grades

def find_grade(score, thresholds, grades):
    idx = bisect.bisect_right(thresholds, score) - 1
    if idx < 0:
        return grades[0]
    if idx >= len(grades):
        return grades[-1]
    return grades[idx]

if __name__ == '__main__':
    thresholds, grades = get_grading_scale()
    sample_score = 85
    result = find_grade(sample_score, thresholds, grades)
    print(result)