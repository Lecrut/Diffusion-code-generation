import bisect

THRESHOLDS = [90, 80, 70, 60, 0]
GRADES = ['A', 'B', 'C', 'D', 'F']

def get_grades():
    return {f"{t}-{THRESHOLDS[i-1] - 1 if i > 0 else 100}": GRADES[i] for i, t in enumerate(THRESHOLDS)}

def lookup_grade(score, thresholds, grades):
    index = bisect.bisect_left(thresholds, score)
    if index < len(thresholds):
        return grades[index]
    return grades[-1]

if __name__ == '__main__':
    scale = get_grades()
    sample_score = 85
    grade = lookup_grade(sample_score, THRESHOLDS, GRADES)
    print(scale)
    print(grade)