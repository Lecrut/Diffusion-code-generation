import bisect

CUTOFFS = [0, 60, 70, 80, 90]
GRADES = ['F', 'D', 'C', 'B', 'A']

def score_to_grade(score: int) -> str:
    if score < 0:
        raise ValueError("Score cannot be negative")
    index = bisect.bisect_right(CUTOFFS, score)
    if index >= len(GRADES):
        return GRADES[-1]
    return GRADES[index]

if __name__ == '__main__':
    test_scores = [55, 65, 75, 85, 95, 100, -5]
    for s in test_scores:
        try:
            print(f"Score {s}: {score_to_grade(s)}")
        except ValueError as e:
            print(f"Score {s}: Error - {e}")