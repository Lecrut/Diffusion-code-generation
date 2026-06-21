import bisect

def get_grading_scale():
    thresholds = [0, 50, 60, 70, 80, 90, 100]
    grades = ['F', 'D', 'C', 'B', 'A', 'A+']
    return dict(zip([f"{t}-{t+thresholds[i+1]-1}" for i, t in enumerate(thresholds[:-1])], grades))

def find_grade(score):
    thresholds = [0, 50, 60, 70, 80, 90, 100]
    grades = ['F', 'D', 'C', 'B', 'A', 'A+']
    index = bisect.bisect_right(thresholds, score) - 1
    index = max(0, min(index, len(grades) - 1))
    return grades[index]

if __name__ == '__main__':
    scale = get_grading_scale()
    sample_score = 85
    grade = find_grade(sample_score)
    print(scale)
    print(grade)