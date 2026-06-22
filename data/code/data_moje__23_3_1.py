import bisect

def score_to_grade(score):
    boundaries = [0, 60, 70, 80, 90]
    grades = ['F', 'D', 'C', 'B', 'A']
    index = bisect.bisect_right(boundaries, score)
    if index < len(grades):
        return grades[index]
    return grades[-1]

if __name__ == '__main__':
    test_scores = [55, 65, 75, 85, 95, 40, 100]
    for s in test_scores:
        grade = score_to_grade(s)
        print(f"Score: {s}, Grade: {grade}")