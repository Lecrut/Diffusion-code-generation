def get_grades(scores_dict):
    grades_dict = {}
    for student, score in scores_dict.items():
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
        grades_dict[student] = grade
    return grades_dict

if __name__ == '__main__':
    scores = {
        'Alice': 95,
        'Bob': 82,
        'Charlie': 74,
        'Diana': 68,
        'Eve': 45
    }
    result = get_grades(scores)
    print(result)