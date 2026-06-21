import bisect

def get_grade(score):
    boundaries = [0, 60, 70, 80, 90]
    grades = ['F', 'D', 'C', 'B', 'A']
    index = bisect.bisect_right(boundaries, score)
    return grades[index]

if __name__ == '__main__':
    test_scores = [45, 65, 72, 88, 95, 100, 59]
    for s in test_scores:
        print(f"{s}: {get_grade(s)}")