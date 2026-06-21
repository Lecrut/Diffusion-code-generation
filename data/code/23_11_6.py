def calculate_grades(scores: dict[str, float]) -> dict[str, str]:
    grades = {}
    for name, score in scores.items():
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        grades[name] = grade
    return grades

if __name__ == '__main__':
    sample_scores = {
        "Alice": 95.0,
        "Bob": 82.5,
        "Charlie": 74.0,
        "Diana": 61.0,
        "Eve": 45.5
    }
    result = calculate_grades(sample_scores)
    print(result)