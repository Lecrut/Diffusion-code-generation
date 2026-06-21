import bisect

def score_to_grade(score, breakpoints, grades):
    idx = bisect.bisect_right(breakpoints, score)
    return grades[idx]

if __name__ == '__main__':
    breakpoints = [0, 60, 70, 80, 90]
    grades = ['F', 'D', 'C', 'B', 'A']
    results = [
        score_to_grade(55, breakpoints, grades),
        score_to_grade(65, breakpoints, grades),
        score_to_grade(75, breakpoints, grades),
        score_to_grade(85, breakpoints, grades),
        score_to_grade(95, breakpoints, grades),
    ]
    print(results)