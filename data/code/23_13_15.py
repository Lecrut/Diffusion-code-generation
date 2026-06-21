import bisect

def get_grade(score, thresholds, grades):
    index = bisect.bisect_right(thresholds, score)
    return grades[index]

def create_grading_scale():
    thresholds = [90, 80, 70, 60]
    grades = ['A', 'B', 'C', 'D', 'F']
    return thresholds, grades

if __name__ == '__main__':
    thresholds, grades = create_grading_scale()
    sample_score = 85
    result = get_grade(sample_score, thresholds, grades)
    print(result)