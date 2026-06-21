import bisect

def get_grading_scale():
    thresholds = [0, 60, 70, 80, 90, 100]
    grades = ['F', 'D', 'C', 'B', 'A']
    return dict(zip(grades, [[thresholds[i], thresholds[i+1]] for i in range(len(thresholds)-1)]))

def lookup_grade(score, thresholds, grades):
    idx = bisect.bisect_right(thresholds, score) - 1
    if idx < 0:
        return grades[0]
    if idx >= len(grades):
        return grades[-1]
    return grades[idx]

if __name__ == '__main__':
    thresholds = [0, 60, 70, 80, 90, 100]
    grades = ['F', 'D', 'C', 'B', 'A']
    sample_score = 85
    result_grade = lookup_grade(sample_score, thresholds, grades)
    print(result_grade)