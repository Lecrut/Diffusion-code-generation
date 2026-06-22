import bisect

SCORES = [0, 60, 70, 80, 90]
GRADES = ['F', 'D', 'C', 'B', 'A']

def get_grade(score):
    if score < 0:
        return 'F'
    if score > 100:
        return 'A'
    index = bisect.bisect_right(SCORES, score) - 1
    return GRADES[index]

if __name__ == '__main__':
    test_scores = [59, 60, 75, 88, 95, 100, -5, 101]
    for s in test_scores:
        print(get_grade(s))