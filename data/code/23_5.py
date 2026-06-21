import operator

def grade_scores(scores):
    thresholds = [(90, 'A'), (80, 'B'), (70, 'C'), (60, 'D'), (0, 'F')]
    return [next(g for m, g in thresholds if s >= m) for s in scores]

if __name__ == '__main__':
    sample_scores = [95, 82, 74, 60, 55, 88, 91, 79]
    result = grade_scores(sample_scores)
    print(result)