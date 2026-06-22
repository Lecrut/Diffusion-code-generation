import bisect

def get_grade(score, thresholds=None, grades=None):
    if thresholds is None:
        thresholds = [0, 60, 70, 80, 90, 100]
    if grades is None:
        grades = ['F', 'D', 'C', 'B', 'A']
    idx = bisect.bisect_right(thresholds, score) - 1
    if idx < 0:
        idx = 0
    if idx >= len(grades):
        idx = len(grades) - 1
    return grades[idx]

def build_grading_scale():
    thresholds = [0, 60, 70, 80, 90, 100]
    grades = ['F', 'D', 'C', 'B', 'A']
    scale = {}
    for i in range(len(thresholds) - 1):
        lower = thresholds[i]
        upper = thresholds[i + 1]
        if i == len(thresholds) - 2:
            key = f"{lower}-{upper}"
        else:
            key = f"{lower}-{upper-1}"
        scale[key] = grades[i]
    return scale

def get_grade_by_binary_search(score):
    thresholds = [0, 60, 70, 80, 90, 100]
    grades = ['F', 'D', 'C', 'B', 'A']
    idx = bisect.bisect_right(thresholds, score) - 1
    if idx < 0:
        idx = 0
    if idx >= len(grades):
        idx = len(grades) - 1
    return grades[idx]

if __name__ == '__main__':
    scale = build_grading_scale()
    print(scale)
    sample_score = 85
    grade = get_grade_by_binary_search(sample_score)
    print(grade)