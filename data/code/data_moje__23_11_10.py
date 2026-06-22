def get_grade(score: float) -> str:
    if score >= 90:
        return 'A'
    if score >= 80:
        return 'B'
    if score >= 70:
        return 'C'
    if score >= 60:
        return 'D'
    return 'F'

scores: dict[str, float] = {
    "Alice": 85.5,
    "Bob": 59.0,
    "Charlie": 92.0,
    "Diana": 73.5,
    "Eve": 100.0
}

def compute_grades(data: dict[str, float]) -> dict[str, str]:
    return {name: get_grade(score) for name, score in data.items()}

if __name__ == '__main__':
    result: dict[str, str] = compute_grades(scores)
    for name, grade in result.items():
        print(f"{name}: {grade}")