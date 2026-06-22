def compute_grades(scores: dict[str, float]) -> dict[str, str]:
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
        "Charlie": 76.0,
        "Diana": 68.0,
        "Eve": 45.0
    }
    result = compute_grades(sample_scores)
    print(result)