import operator

def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def vectorize_grades(scores):
    grade_map = [
        (90, 'A'),
        (80, 'B'),
        (70, 'C'),
        (60, 'D'),
        (0, 'F')
    ]
    return [next(grade for threshold, grade in grade_map if score >= threshold) for score in scores]

if __name__ == '__main__':
    sample_scores = [95, 82, 67, 55, 90, 78]
    result = vectorize_grades(sample_scores)
    print(result)