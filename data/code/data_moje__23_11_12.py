def calculate_grades(scores: dict[str, float]) -> dict[str, str]:
    grades = {}
    for student, score in scores.items():
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
        grades[student] = grade
    return grades

if __name__ == '__main__':
    sample_scores = {
        "Alice": 95.5,
        "Bob": 82.0,
        "Charlie": 74.3,
        "Diana": 68.9,
        "Eve": 45.0
    }
    result = calculate_grades(sample_scores)
    print(result)