import operator

def score_to_grade(score):
    if score >= 90:
        return 'A'
    if score >= 80:
        return 'B'
    if score >= 70:
        return 'C'
    if score >= 60:
        return 'D'
    return 'F'

def convert_scores_to_grades(scores):
    mapping = [
        (90, 'A'),
        (80, 'B'),
        (70, 'C'),
        (60, 'D'),
        (0, 'F')
    ]
    grades = []
    for score in scores:
        for threshold, grade in mapping:
            if score >= threshold:
                grades.append(grade)
                break
    return grades

if __name__ == '__main__':
    sample_scores = [95, 82, 77, 59, 68, 100, 45, 91]
    result = convert_scores_to_grades(sample_scores)
    print(result)