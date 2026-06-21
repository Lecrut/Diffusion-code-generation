import bisect

THRESHOLDS = [0, 60, 70, 80, 90]
GRADES = ['F', 'D', 'C', 'B', 'A']

def get_grades():
    return {f"{THRESHOLDS[i]}-{THRESHOLDS[i+1]-1}": GRADES[i] for i in range(len(GRADES) - 1)} | {f"{THRESHOLDS[-1]}+": GRADES[-1]}

def get_grade(score):
    index = bisect.bisect_right(THRESHOLDS, score) - 1
    if index < 0:
        index = 0
    if index >= len(GRADES):
        index = len(GRADES) - 1
    return GRADES[index]

if __name__ == '__main__':
    scale = get_grades()
    print(scale)
    score = 85
    grade = get_grade(score)
    print(f"Score {score} -> {grade}")