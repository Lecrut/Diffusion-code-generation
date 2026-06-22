import operator

def get_grade(score):
    if score >= 90:
        return 'A'
    if score >= 80:
        return 'B'
    if score >= 70:
        return 'C'
    if score >= 60:
        return 'D'
    return 'F'

def score_to_grades(scores):
    return list(map(get_grade, scores))

if __name__ == '__main__':
    sample_scores = [95, 82, 67, 54, 91, 78, 45, 100, 89, 72]
    grades = score_to_grades(sample_scores)
    print(grades)