import bisect

def get_grade(score):
    boundaries = [0, 60, 70, 80, 90]
    grades = ["F", "D", "C", "B", "A"]
    index = bisect.bisect_right(boundaries, score)
    if index == 0:
        return "F"
    return grades[index - 1]

if __name__ == "__main__":
    sample_scores = [45, 65, 75, 85, 95, 0, 100, 59, 60]
    for s in sample_scores:
        print(get_grade(s))