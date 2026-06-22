import bisect

score_grade_tuples = [
    (90, 'A'),
    (80, 'B'),
    (70, 'C'),
    (60, 'D'),
    (0, 'F')
]

score_thresholds = sorted([(s, g) for s, g in score_grade_tuples], key=lambda x: x[0])
grades_lookup = sorted([g for _, g in score_thresholds], reverse=True)
scores_lookup = sorted([s for s, _ in score_thresholds], reverse=True)

def get_grade(score):
    index = bisect.bisect_left(scores_lookup, score)
    if index < len(grades_lookup):
        return grades_lookup[index]
    return 'F'

if __name__ == '__main__':
    test_scores = [95, 85, 75, 65, 55, 100]
    results = list(map(lambda s: get_grade(s), test_scores))
    print(results)