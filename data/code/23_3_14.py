import bisect

def get_grade(score):
    boundaries = [60, 70, 80, 90]
    grades = ['D', 'C', 'B', 'A']
    index = bisect.bisect_right(boundaries, score)
    if score < 60:
        return 'F'
    return grades[index]

if __name__ == '__main__':
    test_scores = [55, 65, 75, 85, 95, 42]
    results = [get_grade(s) for s in test_scores]
    for score, grade in zip(test_scores, results):
        print(f"Score: {score}, Grade: {grade}")