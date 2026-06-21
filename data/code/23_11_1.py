def get_grade(score: int) -> str:
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

if __name__ == '__main__':
    scores = {'Alice': 95, 'Bob': 82, 'Charlie': 67, 'Diana': 58, 'Eve': 88}
    grades = {name: get_grade(score) for name, score in scores.items()}
    print(grades)