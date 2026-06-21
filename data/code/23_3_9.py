import bisect

def get_grade(score):
    grade_boundaries = [0, 60, 70, 80, 90, 100]
    grades = ['F', 'D', 'C', 'B', 'A']
    index = bisect.bisect_right(grade_boundaries, score) - 1
    if index < 0:
        return grades[0]
    if index >= len(grades):
        return grades[-1]
    return grades[index]

if __name__ == '__main__':
    sample_scores = [55, 65, 75, 85, 95, 100, 105, -5]
    for s in sample_scores:
        print(f"Score {s}: {get_grade(s)}")