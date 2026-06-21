import bisect

def get_grade(score):
    thresholds = [60, 70, 80, 90]
    grades = ['D', 'C', 'B', 'A']
    if score < 60:
        return 'F'
    index = bisect.bisect_right(thresholds, score)
    return grades[index]

def build_grading_scale():
    thresholds = [60, 70, 80, 90]
    grades = ['D', 'C', 'B', 'A']
    scale = {}
    scale['fail'] = 'Score < 60'
    for i in range(len(thresholds)):
        start = thresholds[i]
        if i + 1 < len(thresholds):
            end = thresholds[i + 1]
        else:
            end = 100
        scale[f'{start}-{end}'] = grades[i]
    return scale

if __name__ == '__main__':
    sample_score = 85
    result = get_grade(sample_score)
    print(result)