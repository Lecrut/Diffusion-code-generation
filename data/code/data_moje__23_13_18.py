import bisect

def get_grading_scale():
    return {
        "A": (90, 100),
        "B": (80, 89),
        "C": (70, 79),
        "D": (60, 69),
        "F": (0, 59)
    }

def find_grade_for_score(score, thresholds, grades):
    index = bisect.bisect_right(thresholds, score) - 1
    if index < 0:
        return grades[0]
    if index >= len(grades):
        return grades[-1]
    return grades[index]

if __name__ == '__main__':
    thresholds = [60, 70, 80, 90, 100]
    grades = ["F", "D", "C", "B", "A"]
    sample_score = 85
    grade = find_grade_for_score(sample_score, thresholds, grades)
    print(grade)