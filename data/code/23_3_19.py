import bisect

GRADE_BOUNDARIES = [50, 60, 70, 80, 90]
GRADE_LABELS = ["Fail", "Pass", "Credit", "Distinction", "High Distinction"]

def get_grade(score):
    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100")
    index = bisect.bisect_right(GRADE_BOUNDARIES, score)
    return GRADE_LABELS[index]

if __name__ == "__main__":
    sample_scores = [45, 55, 65, 75, 85, 95]
    for s in sample_scores:
        print(get_grade(s))