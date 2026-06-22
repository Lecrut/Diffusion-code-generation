import bisect

THRESHOLDS = [0, 60, 70, 80, 90]
GRADES = ['F', 'D', 'C', 'B', 'A']

def get_grade(score):
    idx = bisect.bisect_right(THRESHOLDS, score) - 1
    if idx < 0:
        idx = 0
    if idx >= len(GRADES):
        idx = len(GRADES) - 1
    return {
        "score": score,
        "grade": GRADES[idx],
        "thresholds": THRESHOLDS
    }

if __name__ == '__main__':
    result = get_grade(85)
    print(result)