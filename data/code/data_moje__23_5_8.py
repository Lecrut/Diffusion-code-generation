import math

def calculate_grades(scores):
    if not scores:
        return []
    max_score = max(scores)
    if max_score == 0:
        return [0 for _ in scores]
    multiplier = 100.0 / max_score
    grades = []
    for score in scores:
        percent = score * multiplier
        if percent >= 90:
            grades.append('A')
        elif percent >= 80:
            grades.append('B')
        elif percent >= 70:
            grades.append('C')
        elif percent >= 60:
            grades.append('D')
        else:
            grades.append('F')
    return grades

if __name__ == '__main__':
    sample_scores = [45, 67, 89, 23, 100, 55, 92, 78]
    result = calculate_grades(sample_scores)
    print(result)