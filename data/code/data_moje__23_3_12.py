import bisect

def score_to_grade(score):
    boundaries = [0, 40, 50, 60, 70, 80, 90]
    grades = ['F', 'D', 'C', 'B', 'A', 'A+', 'A++']
    index = bisect.bisect_right(boundaries, score)
    return grades[index]

if __name__ == '__main__':
    scores = [35, 45, 55, 65, 75, 85, 95, 100]
    for s in scores:
        result = score_to_grade(s)
        print(f"Score {s}: {result}")