import bisect

def get_grade(score):
    boundaries = [0, 60, 70, 80, 90]
    grades = ['F', 'D', 'C', 'B', 'A']
    index = bisect.bisect_right(boundaries, score)
    if index >= len(grades):
        return 'A+'
    return grades[index]

if __name__ == '__main__':
    test_scores = [59, 60, 65, 74, 89, 95, 100, 110]
    for s in test_scores:
        print(get_grade(s))