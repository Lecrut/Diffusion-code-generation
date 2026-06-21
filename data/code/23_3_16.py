import bisect

SCORE_BOUNDARIES = [0, 50, 60, 70, 80, 90]
GRADE_LABELS = ["F", "D", "C", "B", "A", "A+"]

def map_score_to_grade(score: float) -> str:
    index = bisect.bisect_right(SCORE_BOUNDARIES, score)
    return GRADE_LABELS[index] if index < len(GRADE_LABELS) else "A+"

if __name__ == '__main__':
    scores = [45, 50, 65, 75, 85, 95, 100]
    for s in scores:
        grade = map_score_to_grade(s)
        print(f"Score: {s}, Grade: {grade}")