import bisect

SCORE_THRESHOLDS = [90, 80, 70, 60, 0]
GRADE_MAP = ['A', 'B', 'C', 'D', 'F']

def get_grade(score: int) -> str:
    idx = bisect.bisect_left(SCORE_THRESHOLDS, score)
    if idx < len(GRADE_MAP):
        return GRADE_MAP[idx]
    return GRADE_MAP[-1]

def main():
    score = 85
    grade = get_grade(score)
    print(grade)

if __name__ == '__main__':
    main()