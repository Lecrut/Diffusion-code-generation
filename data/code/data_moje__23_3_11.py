import bisect

def score_to_grade(score):
    boundaries = [0, 60, 70, 80, 90, 100]
    grades = ['F', 'D', 'C', 'B', 'A']
    index = bisect.bisect_right(boundaries, score) - 1
    if index < 0:
        return 'F'
    if index >= len(grades):
        return 'A'
    return grades[index]

if __name__ == '__main__':
    sample_scores = [0, 59, 60, 65, 75, 85, 95, 100, -5, 105]
    for s in sample_scores:
        print(score_to_grade(s))