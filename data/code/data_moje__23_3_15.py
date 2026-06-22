import bisect

def get_grade(score):
    boundaries = [90, 80, 70, 60]
    grades = ['A', 'B', 'C', 'D', 'F']
    index = bisect.bisect_left(boundaries, score)
    return grades[index]

if __name__ == '__main__':
    sample_scores = [95, 85, 72, 65, 50, 100]
    for s in sample_scores:
        print(get_grade(s))