import bisect

def get_grade(score):
    boundaries = [0, 60, 70, 80, 90]
    grades = ['F', 'D', 'C', 'B', 'A']
    index = bisect.bisect_right(boundaries, score)
    if index >= len(grades):
        return 'A'
    return grades[index]

if __name__ == '__main__':
    samples = [45, 60, 65, 75, 85, 95]
    for s in samples:
        print(get_grade(s))