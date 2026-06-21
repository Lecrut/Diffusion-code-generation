def get_grades(scores: dict[str, int]) -> dict[str, str]:
    grades = {}
    for name, score in scores.items():
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
        grades[name] = grade
    return grades

if __name__ == '__main__':
    sample_scores = {
        'Alice': 92,
        'Bob': 85,
        'Charlie': 78,
        'Diana': 65,
        'Eve': 55
    }
    print(get_grades(sample_scores))