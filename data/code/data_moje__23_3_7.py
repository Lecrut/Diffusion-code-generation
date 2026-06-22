import bisect

SCORE_THRESHOLDS = [
    0, 40, 50, 60, 70, 80, 90
]

GRADE_LETTERS = [
    "F", "D", "C", "B", "A", "A+", "S"
]

def get_grade(score: float) -> str:
    index = bisect.bisect_right(SCORE_THRESHOLDS, score) - 1
    if index < 0:
        index = 0
    if index >= len(GRADE_LETTERS):
        index = len(GRADE_LETTERS) - 1
    return GRADE_LETTERS[index]

if __name__ == '__main__':
    scores = [35, 45, 55, 65, 75, 85, 95, 100, -5]
    for score in scores:
        result = get_grade(score)
        print(f"Score: {score} -> Grade: {result}")