def scores_to_grades(scores: dict) -> dict:
    grades = {}
    for key, score in scores.items():
        if score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        elif score >= 60:
            grade = 'D'
        else:
            grade = 'F'
        grades[key] = grade
    return grades

if __name__ == '__main__':
    predefined_scores = {
        'Alice': 92,
        'Bob': 85,
        'Charlie': 74,
        'Diana': 68,
        'Eve': 45
    }
    result = scores_to_grades(predefined_scores)
    print(result)