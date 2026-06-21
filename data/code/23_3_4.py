import bisect

def score_to_grade(score, thresholds=(60, 70, 80, 90), grades=('F', 'D', 'C', 'B', 'A')):
    idx = bisect.bisect_right(thresholds, score)
    return grades[idx]

if __name__ == '__main__':
    scores = [55, 62, 75, 88, 95, 100]
    for s in scores:
        print(score_to_grade(s))