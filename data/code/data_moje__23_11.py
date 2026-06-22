def calculate_grade(score: int) -> str:
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def grade_scores(scores: dict[str, int]) -> dict[str, str]:
    return {name: calculate_grade(score) for name, score in scores.items()}

if __name__ == "__main__":
    sample_scores = {
        "Alice": 95,
        "Bob": 82,
        "Charlie": 77,
        "Diana": 64,
        "Eve": 59
    }
    results = grade_scores(sample_scores)
    for name, grade in results.items():
        print(f"{name}: {grade}")