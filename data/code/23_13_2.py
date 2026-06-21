import bisect

def get_grade_scale():
    thresholds = [90, 80, 70, 60, 0]
    grades = ['A', 'B', 'C', 'D', 'F']
    return thresholds, grades

def find_grade(score, thresholds, grades):
    index = bisect.bisect_right(thresholds, score)
    if index >= len(grades):
        return grades[-1]
    return grades[index]

def generate_grading_scale():
    thresholds, grades = get_grade_scale()
    scale = {}
    for i in range(len(thresholds)):
        if i == len(thresholds) - 1:
            scale[(0, thresholds[i])] = grades[i]
        else:
            scale[(thresholds[i+1], thresholds[i])] = grades[i]
    return scale

def get_grade_for_score(score):
    thresholds, grades = get_grade_scale()
    return find_grade(score, thresholds, grades)

if __name__ == '__main__':
    sample_score = 85
    result = get_grade_for_score(sample_score)
    print(result)