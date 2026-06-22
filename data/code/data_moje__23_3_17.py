import bisect

BORDER = [0, 60, 70, 80, 90]
GRADE = ["F", "D", "C", "B", "A"]

def score_to_grade(score: float) -> str:
    idx = bisect.bisect_right(BORDER, score)
    return GRADE[idx]

if __name__ == '__main__':
    sample_scores = [55, 65, 75, 85, 95, 100]
    for s in sample_scores:
        result = score_to_grade(s)
        print(f"Score {s} -> {result}")