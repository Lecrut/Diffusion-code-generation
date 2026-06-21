import bisect

def get_grading_scale():
    thresholds = [0, 60, 70, 80, 90, 100]
    grades = ['F', 'D', 'C', 'B', 'A']
    return dict(zip(grades, [[thresholds[i], thresholds[i + 1]] for i in range(len(grades))]))

def get_grade_for_score(score, thresholds, grades):
    index = bisect.bisect_right(thresholds, score) - 1
    if index < 0:
        return grades[0]
    if index >= len(grades):
        return grades[-1]
    return grades[index]

if __name__ == '__main__':
    thresholds = [0, 60, 70, 80, 90, 100]
    grades = ['F', 'D', 'C', 'B', 'A']
    sample_score = 85
    grade = get_grade_for_score(sample_score, thresholds, grades)
    print(grade)