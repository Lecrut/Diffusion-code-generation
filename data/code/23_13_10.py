import bisect

def get_grading_scale():
    lower_bounds = [0, 60, 70, 80, 90]
    grades = ['F', 'D', 'C', 'B', 'A']
    return dict(zip(grades, lower_bounds))

def get_grade(score, thresholds):
    index = bisect.bisect_right(thresholds, score)
    return index

if __name__ == '__main__':
    thresholds = [0, 60, 70, 80, 90]
    sample_score = 85
    index = get_grade(sample_score, thresholds)
    grades = ['F', 'D', 'C', 'B', 'A']
    if index < len(grades):
        result_grade = grades[index]
    else:
        result_grade = grades[-1]
    print({result_grade: min(t for t in thresholds if t > sample_score) if index > 0 else 0})
    print(get_grading_scale())