import bisect

def score_to_grade(score):
    boundaries = [0, 60, 70, 80, 90, 100]
    grades = ['F', 'D', 'C', 'B', 'A']
    index = bisect.bisect_right(boundaries, score) - 1
    if index < 0:
        return grades[0]
    if index >= len(grades):
        return grades[-1]
    return grades[index]

if __name__ == '__main__':
    print(score_to_grade(55))
    print(score_to_grade(60))
    print(score_to_grade(75))
    print(score_to_grade(88))
    print(score_to_grade(95))
    print(score_to_grade(100))
    print(score_to_grade(-5))
    print(score_to_grade(105))